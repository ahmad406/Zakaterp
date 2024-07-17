import frappe
import json
import base64
from frappe.utils.data import flt

@frappe.whitelist()
def resubmit_submit(inv):
	doc=frappe.get_doc("Sales Invoice",inv)
	if doc.docstatus!=1:
		frappe.throw("Document state is not submitted")
	else:
		before_submit(doc,resubmit=1,method=None)

@frappe.whitelist()
def before_submit(doc,method=None,resubmit=0):
	import requests
	import json
	data = {}
	data["is_customer_address"] = False
	data["zatca_status"] = doc.zatca_status
	data["resubmit_zatca"] = resubmit
	if doc.bill_type=="B2B" and not doc.delivery_date:
			frappe.throw("Delivery Date is missing..")

	if doc.customer_address:
		add = frappe.get_doc("Address", doc.customer_address)
		data["city"] = add.city
		data["pin_code"] = add.pincode
		data["state"] = add.state
		data["street"] = add.address_line1
		data["building_no"] = add.building_no
		data["plot_id_no"] = add.plot_id_no
		data['city_subdivision_name']=add.city_subdivision_name
		data["is_customer_address"]=True
	data["company"] = doc.company
	data["crn"] = frappe.db.get_value('Customer', doc.customer, 'crn')
	data["customer_tax_id"] = frappe.db.get_value('Customer', doc.customer, 'tax_id')
	data["actual_delivery_date"] = doc.delivery_date
	data["due_date"] = doc.due_date
	data['customer']=doc.customer
	data['customer_name']=doc.customer_name
	data["name"] = doc.name
	data["posting_date"] = doc.posting_date
	data["posting_time"] = doc.posting_time
	data["total_taxes_and_charges"]=round(doc.total_taxes_and_charges ,2)
	data["net_total"]=round(doc.net_total ,2)
	data["total"]=round(doc.total ,2)
	data["grand_total"]=round(doc.grand_total ,2)
	data["ref"] = doc.return_against
	if doc.apply_discount_on=='Grand Total' and doc.discount_amount>0:
		frappe.throw("Discount can't be applied on  Grand Total")
	data["items"] = []
	for item in doc.items:
		data["items"].append(item.as_dict())
		tx_rate=0
		for idx,f in enumerate(doc.taxes):
			if frappe.db.get_value('Account', f.account_head, 'account_type')=="Tax":
				for item_code, (rate, amount) in   json.loads(doc.taxes[idx].item_wise_tax_detail).items():
					if item_code==item.item_code:
								data["items"][(item.idx-1)].taxes_amount=(round(abs(float(amount)) , 2)) 
								data["items"][(item.idx-1)].taxes_percentage= (round(abs(float(rate)) , 2)) 
								tx_rate= abs(float(rate))
				data["vat_rate"]=tx_rate
			else:
				data["additional_charge"]=round(abs(float(f.tax_amount)) ,2)
	if doc.is_return:
		data["invoice_type"] ="Credit Note"
	else:
		data["invoice_type"]="Invoice"
	data["bill_type"]=doc.bill_type
	data["additional_charge"]=round(abs(float(doc.zatca_additional)) ,2)
	data["total_taxes_and_charges"]=round(abs(doc.zatca_taxamount) ,2)
	data["discount"]=round(abs((doc.zatca_discount)),2)
	data["total"]=round(doc.rounded_total ,2) if round(doc.rounded_total ,2) else round(doc.grand_total ,2)
	data["currency"]=doc.currency
	# if doc.rounded_total==doc.grand_total and doc.rounding_adjustment!=0:
	#     # data["grand_total"]=round(doc.rounded_total-doc.rounding_adjustment,2)
	#     data["grand_total"]=round(doc.net_total+doc.total_taxes_and_charges,2)
	data["base_total_taxes_and_charges"]=flt(abs(float((doc.zatca_taxamount*doc.conversion_rate))) ,2)


			
			
	data["rounding_adjustment"]=((doc.rounding_adjustment))
	token=None
	url=None
	if doc.company=="ARKAN BARWAH CONTRACTING EST":
		token="token 15a67b38e5fe7f6:097b5b51793aeb9"
		url ="https://arkan.zakat.etoserp.com/api/method/stand_alone.api.send_zakat"


	if doc.company=="ARKAN BARWAH Est. FOR THE TRANSPORTATION OF GOODS":
		url = "https://palmlogistics.zakat.etoserp.com/api/method/stand_alone.api.send_zakat"
		token="token 0e76b7b591d4c4b:d21ab6425f08835"

	if doc.company=="FREIGHT WORLD AL OFI CO., OPC":
		url = "https://zakat.freightworld.etoserp.com/api/method/stand_alone.api.send_zakat"
		token="token 10079d58801d2d2:097b5b51793aeb9"



	if not token:
		frappe.throw("Token Missing")
	json_data = json.dumps({"data": data}, default=str)
	headers = {
	'Authorization':token,
	'Content-Type': 'application/json',
	'Cookie': 'sid=Guest'
	}


	response = requests.request("POST",url, headers=headers, data=json_data)
	res=json.loads(response.text)
	filename = "{0}_signed.xml".format(doc.name)
	doctype = doc.doctype
	docname = doc.name 
	folder = 'Home/Attachments' 
	if doc.bill_type=="B2B":
		updated=0
		if res["message"].get("clearanceStatus")=="NOT_CLEARED":
			doc.db_set("zatca_status","Clearance Failed",update_modified=False)
			updated=1
			frappe.throw("Clearance Failed")
		elif res["message"].get("reportingStatus")=="NOT_REPORTED":
			doc.db_set("zatca_status","Reporting Failed",update_modified=False)
			updated=1
			frappe.throw("Reporting Failed")
		if updated==0:
			if res["message"]["Status"]=="CLEARED":
				doc.db_set("zatca_status","CLEARED",update_modified=False)
				filedata_decoded =(base64.b64decode(res["message"]["response"]["clearedInvoice"]).decode('utf-8'))
				doc.db_set("hash_qr",res["message"]["qr"],update_modified=False)
				attachment_info = attach_file(
					filename=filename,
					doctype=doctype,
					docname=docname,
					folder=folder,
					decode_base64=False,
					is_private=None,
					docfield=None,
					filedata_decoded=filedata_decoded
				)
			if res["message"]["Status"]=="REPORTED":
				doc.db_set("zatca_status","REPORTED",update_modified=False)
				filedata_decoded =(base64.b64decode(res["message"]["inv"]).decode('utf-8'))
				doc.db_set("hash_qr",res["message"]["qr"],update_modified=False)
				attachment_info = attach_file(
					filename=filename,
					doctype=doctype,
					docname=docname,
					folder=folder,
					decode_base64=False,
					is_private=None,
					docfield=None,
					filedata_decoded=filedata_decoded
				)



	else:
		if res["message"]==0:
			doc.db_set("zatca_status","Reporting Failed",update_modified=False)
			frappe.throw("Reporting Failed")
		else:
			if res["message"]["res"]["reportingStatus"]=="REPORTED":
				doc.db_set("zatca_status","REPORTED",update_modified=False)
				doc.db_set("hash_qr",res["message"]["qr"],update_modified=False)
				filedata_decoded =((res["message"]["hash_inv"]))
				attachment_info = attach_file(
					filename=filename,
					doctype=doctype,
					docname=docname,
					folder=folder,
					decode_base64=False,
					is_private=None,
					docfield=None,
					filedata_decoded=filedata_decoded
				)

def attach_file(filename=None, doctype=None, docname=None, folder=None, decode_base64=False, is_private=0, docfield=None,filedata_decoded=None):
	from frappe.utils.file_manager import save_file
	doc = frappe.get_doc(doctype, docname)
	f = save_file(filename, filedata_decoded.encode('utf-8'), doctype, docname, folder, decode_base64, is_private, docfield)
	if docfield and doctype:
		doc.set(docfield, f.file_url)
		doc.save()

	return f.as_dict()
@frappe.whitelist()
def correct_vat(name):
	so=frappe.get_doc("Sales Invoice",name)
	validate(so)

def validate(self,method=None):

	tx=validate_multiple_tax(self)
	if tx:
		self.zatca_taxamount=tx.tax_amount
		if self.docstatus==1:
			self.db_set("zatca_taxamount",tx.tax_amount,update_modified=False)

		self.zatca_discount=0
		self.zatca_additional=0
		if tx.charge_type!="On Net Total":
			n=int(tx.row_id)
			discount=0
			additional=0
			for i in self.taxes:
				if i.idx  <=n:
					taxamt=i.tax_amount
					if self.is_return:
						if taxamt<0:
							additional+=taxamt
						else:
							discount+=taxamt
					else:
						if taxamt>0:
							additional+=taxamt
						else:
							discount+=taxamt
			

			self.zatca_discount=discount
			self.zatca_additional=additional
			if self.docstatus==1:
				self.db_set("zatca_discount",discount,update_modified=False)
				self.db_set("zatca_additional",additional,update_modified=False)
				 
			print(discount,additional,self.zatca_taxamount,"op")
	else:
		if self.docstatus==1:
			self.db_set("zatca_taxamount",0,update_modified=False)
		print(self.zatca_taxamount)
		self.zatca_taxamount=0
		print(self.zatca_taxamount,"2")



	





	

def validate_multiple_tax(self):
	tax_account_count=0
	tx=None
	if self.is_return:
		for d in self.taxes:
			if frappe.db.get_value('Account', d.account_head, 'account_type')=="Tax" and d.tax_amount < 0:
				tax_account_count+=1
				tx=d
	else:
	
		for d in self.taxes:
			if frappe.db.get_value('Account', d.account_head, 'account_type')=="Tax" and d.tax_amount > 0:
				tax_account_count+=1
				tx=d

	if tax_account_count >1:
		frappe.throw("Multiple Tax Account Found!")
	# if tax_account_count ==0:
	# 	frappe.throw("No Tax Account Found!")
	return tx




# def get_length_count(data):
# 	import re
# 	count = len(re.findall(r'\d', data))
# 	return(count)