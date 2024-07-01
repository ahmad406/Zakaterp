frappe.ui.form.on('Sales Invoice', {
    refresh: function(frm) {
        let data=["Clearance Failed","Reporting Failed"]

        if(!frm.is_new() && frm.doc.docstatus==1 &&(data.includes(cur_frm.doc.zatca_status)|| !cur_frm.doc.zatca_status)){
            cur_frm.add_custom_button(__("Resubmit To Zatca"), function () {
                frappe.call({
                    method: "zakaterp.custom_script.sales_invoice.sales_invoice.resubmit_submit",
                    args:{"inv":frm.doc.name},
                    freeze: true,
                    callback: function (r) {
                        frappe.msgprint(__('Submitted successfully'));

                    }
                });
            });
        }
     
    },
})