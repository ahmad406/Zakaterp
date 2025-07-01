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

frappe.whitelist()
def before_submit(doc, method=None, resubmit=0):
	import requests
	data = {
		"is_customer_address": False,
		"zatca_status": doc.zatca_status,
		"resubmit_zatca": resubmit,
		"company": "ALMATALIQ ALRAQIAH TRADING EST",
		"name": doc.name,
		"posting_date": doc.posting_date,
		"posting_time": doc.posting_time,
		"total_taxes_and_charges": round(doc.total_taxes_and_charges, 2),
		"net_total": round(doc.net_total, 2),
		"total": round(doc.total, 2),
		"grand_total": round(doc.grand_total, 2),
		"ref": doc.return_against,
		"customer": doc.customer,
		"customer_name": doc.customer_name,
		"actual_delivery_date": doc.delivery_date,
		"due_date": doc.due_date,
		"currency": doc.currency,
		"items": [],
		"rounding_adjustment": doc.rounding_adjustment
	}

	if frappe.db.get_value('Customer', doc.customer, 'bill_type') == "B2B" and not doc.delivery_date:
		frappe.throw("Delivery Date is missing.")

	if doc.customer_address:
		add = frappe.get_doc("Address", doc.customer_address)
		data.update({
			"country_code": (frappe.db.get_value('Country', add.country, 'code') or 'SA').upper(),
			"city": add.city,
			"pin_code": add.pincode,
			"state": add.state,
			"street": add.address_line1,
			"building_no": add.building_no,
			"plot_id_no": add.plot_id_no,
			"city_subdivision_name": add.city_subdivision_name,
			"is_customer_address": True
		})
		if get_length_count(add.pincode) != 5:
			frappe.throw("Incorrect Customer Postal Code")

	crn_custom = frappe.db.get_value('Customer', doc.customer, 'crn')
	if get_length_count(crn_custom) != 10:
		frappe.throw("Incorrect Customer CRN")
	data["crn"] = crn_custom
	data["customer_tax_id"] = frappe.db.get_value('Customer', doc.customer, 'tax_id')

	if doc.apply_discount_on == 'Grand Total' and doc.discount_amount > 0:
		frappe.throw("Discount can't be applied on Grand Total")

	data["invoice_type"] = "Credit Note" if doc.is_return else "Invoice"
	data["bill_type"] = frappe.db.get_value('Customer', doc.customer, 'bill_type')

	# Tax info mapping
	tx_rate = 0.0

	for item in doc.items:
		itm = item.as_dict()
		itm["taxes_amount"] = 0.0
		itm["taxes_percentage"] = 0.0
		itm["additional_charges"] = 0.0
		itm["discount"] = 0.0

		for tax in doc.taxes:
			if not tax.custom_item_wise_tax_detail:
				continue

			tax_detail = json.loads(tax.custom_item_wise_tax_detail)

			if str(item.idx) in tax_detail:
				rate, amount, row_id, item_name = tax_detail[str(item.idx)]
				if item_name == item.item_name:  # Extra check to ensure same item
					if frappe.db.get_value('Account', tax.account_head, 'account_type') == "Tax":
						itm["taxes_amount"] = flt(abs(float(amount)), 2)
						itm["taxes_percentage"] = flt(abs(float(rate)), 2)
						tx_rate = abs(float(rate))
						if itm["taxes_percentage"] == 0:
							itm["tax_code"] = item.vat_exemption_reason_code
							itm["exempt_reason"] = item.vat_category
							itm["tax_category"] = item.vat_category_code
							if not item.vat_exemption_reason_code:
								frappe.throw("Tax code missing in row {}".format(item.idx))

							if not item.vat_category:
								frappe.throw("Exempt Reason missing in row {}".format(item.idx))

					else:
						if amount > 0:
							itm["additional_charges"] += flt(abs(float(amount)), 2)
						else:
							itm["discount"] += flt(abs(float(amount)), 2)

		data["items"].append(itm)

	data["vat_rate"] = tx_rate
	data["additional_charge"] = round(abs(float(doc.zatca_additional)), 2)
	data["total_taxes_and_charges"] = round(abs(doc.zatca_taxamount), 2)
	data["discount"] = round(abs(doc.zatca_discount), 2)
	data["total"] = round(doc.rounded_total, 2) if doc.rounded_total else round(doc.grand_total, 2)
	data["base_total_taxes_and_charges"] = flt(abs(float(doc.zatca_taxamount * doc.conversion_rate)), 2)
	data["net_total"] =round(doc.net_total, 2)
	if  len(doc.taxes) >1:
		for k in doc.taxes:
				if frappe.db.get_value('Account', k.account_head, 'account_type')=="Tax" and abs(k.tax_amount) > 0:
					data["net_total"] =abs(flt((float(k.total-k.tax_amount)) , 2))
	token=None
	url=None
	if doc.company=="M. RAQIYA EST.":
		token="token b83c9c3016ca58f:31d13cc3a1dae21"
		url ="https://zakat.com/api/method/stand_alone.api.send_zakat"

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
	if frappe.db.get_value('Customer', doc.customer, 'bill_type')=="B2B":
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




def get_length_count(data):
	import re
	count = len(re.findall(r'\d', data))
	return(count)

