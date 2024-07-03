import frappe
from frappe import _

@frappe.whitelist()
def add_custom():
    custom_fields=get_data()
    for field in custom_fields:
            try:
                frappe.get_doc({
                    "doctype": "Custom Field",
                    "dt": field["dt"],
                    "fieldname": field["fieldname"],
                    "label": field["label"],
                    "fieldtype": field["fieldtype"],
                    "options" :field["options"],
                    "fetch_from":field["fetch_from"],
                    "read_only":field["read_only"],
                    "insert_after": field["insert_after"]
                }).insert(ignore_permissions=True)  
                print(f"Custom field '{field['fieldname']}' created successfully.")
            except Exception as e:
                print(f"Error creating custom field '{field['fieldname']}': {e}")

         


def get_data():
    custom_fields=[
        {
        "_assign": None,
        "_comments": None,
        "_liked_by": None,
        "_user_tags": None,
        "allow_in_quick_entry": 0,
        "allow_on_submit": 0,
        "bold": 0,
        "collapsible": 0,
        "collapsible_depends_on": None,
        "columns": 0,
        "creation": "2024-04-29 12:40:33.759148",
        "default": None,
        "depends_on": None,
        "description": None,
        "docstatus": 0,
        "dt": "Address",
        "fetch_from": None,
        "fetch_if_empty": 0,
        "fieldname": "building_no",
        "fieldtype": "Data",
        "hidden": 0,
        "hide_border": 0,
        "hide_days": 0,
        "hide_seconds": 0,
        "idx": 9,
        "ignore_user_permissions": 0,
        "ignore_xss_filter": 0,
        "in_global_search": 0,
        "in_list_view": 0,
        "in_preview": 0,
        "in_standard_filter": 0,
        "insert_after": "city_subdivision_name",
        "is_system_generated": 0,
        "is_virtual": 0,
        "label": "Building No",
        "length": 0,
        "mandatory_depends_on": None,
        "modified": "2024-04-29 12:43:46.129946",
        "modified_by": "Administrator",
        "module": None,
        "name": "Address-custom_building_no",
        "no_copy": 0,
        "non_negative": 0,
        "options": None,
        "owner": "Administrator",
        "permlevel": 0,
        "precision": "",
        "print_hide": 0,
        "print_hide_if_no_value": 0,
        "print_width": None,
        "read_only": 0,
        "read_only_depends_on": None,
        "report_hide": 0,
        "reqd": 0,
        "search_index": 0,
        "sort_options": 0,
        "translatable": 1,
        "unique": 0,
        "width": None
        },
        {
        "_assign": None,
        "_comments": None,
        "_liked_by": None,
        "_user_tags": None,
        "allow_in_quick_entry": 0,
        "allow_on_submit": 0,
        "bold": 0,
        "collapsible": 0,
        "collapsible_depends_on": None,
        "columns": 0,
        "creation": "2024-04-29 12:40:33.275589",
        "default": None,
        "depends_on": None,
        "description": None,
        "docstatus": 0,
        "dt": "Address",
        "fetch_from": None,
        "fetch_if_empty": 0,
        "fieldname": "plot_id_no",
        "fieldtype": "Data",
        "hidden": 0,
        "hide_border": 0,
        "hide_days": 0,
        "hide_seconds": 0,
        "idx": 7,
        "ignore_user_permissions": 0,
        "ignore_xss_filter": 0,
        "in_global_search": 0,
        "in_list_view": 0,
        "in_preview": 0,
        "in_standard_filter": 0,
        "insert_after": "city",
        "is_system_generated": 0,
        "is_virtual": 0,
        "label": "Plot Id No",
        "length": 0,
        "mandatory_depends_on": None,
        "modified": "2024-04-29 12:43:57.598462",
        "modified_by": "Administrator",
        "module": None,
        "name": "Address-custom_plot_id_no",
        "no_copy": 0,
        "non_negative": 0,
        "options": None,
        "owner": "Administrator",
        "permlevel": 0,
        "precision": "",
        "print_hide": 0,
        "print_hide_if_no_value": 0,
        "print_width": None,
        "read_only": 0,
        "read_only_depends_on": None,
        "report_hide": 0,
        "reqd": 0,
        "search_index": 0,
        "sort_options": 0,
        "translatable": 1,
        "unique": 0,
        "width": None
        },
        {
        "_assign": None,
        "_comments": None,
        "_liked_by": None,
        "_user_tags": None,
        "allow_in_quick_entry": 0,
        "allow_on_submit": 0,
        "bold": 0,
        "collapsible": 0,
        "collapsible_depends_on": None,
        "columns": 0,
        "creation": "2024-04-29 12:40:33.542735",
        "default": None,
        "depends_on": None,
        "description": None,
        "docstatus": 0,
        "dt": "Address",
        "fetch_from": None,
        "fetch_if_empty": 0,
        "fieldname": "city_subdivision_name",
        "fieldtype": "Data",
        "hidden": 0,
        "hide_border": 0,
        "hide_days": 0,
        "hide_seconds": 0,
        "idx": 8,
        "ignore_user_permissions": 0,
        "ignore_xss_filter": 0,
        "in_global_search": 0,
        "in_list_view": 0,
        "in_preview": 0,
        "in_standard_filter": 0,
        "insert_after": "plot_id_no",
        "is_system_generated": 0,
        "is_virtual": 0,
        "label": "City Subdivision Name",
        "length": 0,
        "mandatory_depends_on": None,
        "modified": "2024-04-29 12:43:57.689271",
        "modified_by": "Administrator",
        "module": None,
        "name": "Address-custom_city_subdivision_name",
        "no_copy": 0,
        "non_negative": 0,
        "options": None,
        "owner": "Administrator",
        "permlevel": 0,
        "precision": "",
        "print_hide": 0,
        "print_hide_if_no_value": 0,
        "print_width": None,
        "read_only": 0,
        "read_only_depends_on": None,
        "report_hide": 0,
        "reqd": 0,
        "search_index": 0,
        "sort_options": 0,
        "translatable": 1,
        "unique": 0,
        "width": None
        },
        {
        "_assign": None,
        "_comments": None,
        "_liked_by": None,
        "_user_tags": None,
        "allow_in_quick_entry": 0,
        "allow_on_submit": 0,
        "bold": 0,
        "collapsible": 0,
        "collapsible_depends_on": None,
        "columns": 0,
        "creation": "2023-12-27 16:03:20.960328",
        "default": None,
        "depends_on": None,
        "description": None,
        "docstatus": 0,
        "dt": "Customer",
        "fetch_from": None,
        "fetch_if_empty": 0,
        "fieldname": "crn",
        "fieldtype": "Data",
        "hidden": 0,
        "hide_border": 0,
        "hide_days": 0,
        "hide_seconds": 0,
        "idx": 9,
        "ignore_user_permissions": 0,
        "ignore_xss_filter": 0,
        "in_global_search": 0,
        "in_list_view": 0,
        "in_preview": 0,
        "in_standard_filter": 0,
        "insert_after": "tax_id",
        "is_system_generated": 0,
        "is_virtual": 0,
        "label": "CRN",
        "length": 0,
        "mandatory_depends_on": None,
        "modified": "2023-12-27 16:03:20.960328",
        "modified_by": "Administrator",
        "module": None,
        "name": "Customer-crn",
        "no_copy": 0,
        "non_negative": 0,
        "options": None,
        "owner": "Administrator",
        "permlevel": 0,
        "precision": "",
        "print_hide": 0,
        "print_hide_if_no_value": 0,
        "print_width": None,
        "read_only": 0,
        "read_only_depends_on": None,
        "report_hide": 0,
        "reqd": 0,
        "search_index": 0,
        "translatable": 1,
        "unique": 0,
        "width": None
        },
        {
        "_assign": None,
        "_comments": None,
        "_liked_by": None,
        "_user_tags": None,
        "allow_in_quick_entry": 0,
        "allow_on_submit": 0,
        "bold": 0,
        "collapsible": 0,
        "collapsible_depends_on": None,
        "columns": 0,
        "creation": "2024-04-29 12:45:41.270452",
        "default": None,
        "depends_on": None,
        "description": None,
        "docstatus": 0,
        "dt": "Customer",
        "fetch_from": None,
        "fetch_if_empty": 0,
        "fieldname": "bill_type",
        "fieldtype": "Select",
        "hidden": 0,
        "hide_border": 0,
        "hide_days": 0,
        "hide_seconds": 0,
        "idx": 4,
        "ignore_user_permissions": 0,
        "ignore_xss_filter": 0,
        "in_global_search": 0,
        "in_list_view": 0,
        "in_preview": 0,
        "in_standard_filter": 0,
        "insert_after": "salutation",
        "is_system_generated": 0,
        "is_virtual": 0,
        "label": "Bill Type",
        "length": 0,
        "mandatory_depends_on": None,
        "modified": "2024-04-29 12:47:25.843198",
        "modified_by": "Administrator",
        "module": None,
        "name": "Customer-custom_bill_type",
        "no_copy": 0,
        "non_negative": 0,
        "options": "B2B\nB2C",
        "owner": "Administrator",
        "permlevel": 0,
        "precision": "",
        "print_hide": 0,
        "print_hide_if_no_value": 0,
        "print_width": None,
        "read_only": 0,
        "read_only_depends_on": None,
        "report_hide": 0,
        "reqd": 0,
        "search_index": 0,
        "translatable": 1,
        "unique": 0,
        "width": None
        },
        {
        "_assign": None,
        "_comments": None,
        "_liked_by": None,
        "_user_tags": None,
        "allow_in_quick_entry": 0,
        "allow_on_submit": 0,
        "bold": 0,
        "collapsible": 0,
        "collapsible_depends_on": None,
        "columns": 0,
        "creation": "2024-05-01 09:49:53.684060",
        "default": None,
        "depends_on": None,
        "description": None,
        "docstatus": 0,
        "dt": "Sales Invoice",
        "fetch_from": None,
        "fetch_if_empty": 0,
        "fieldname": "zatca_status",
        "fieldtype": "Select",
        "hidden": 0,
        "hide_border": 0,
        "hide_days": 0,
        "hide_seconds": 0,
        "idx": 209,
        "ignore_user_permissions": 0,
        "ignore_xss_filter": 0,
        "in_global_search": 0,
        "in_list_view": 0,
        "in_preview": 0,
        "in_standard_filter": 0,
        "insert_after": "connections_tab",
        "is_system_generated": 0,
        "is_virtual": 0,
        "label": "Zatca Status",
        "length": 0,
        "mandatory_depends_on": None,
        "modified": "2024-05-01 09:52:24.690241",
        "modified_by": "Administrator",
        "module": None,
        "name": "Sales Invoice-custom_zatca_status",
        "no_copy": 0,
        "non_negative": 0,
        "options": "\nREPORTED\nCLEARED\nClearance Failed\nReporting Failed",
        "owner": "Administrator",
        "permlevel": 0,
        "precision": "",
        "print_hide": 0,
        "print_hide_if_no_value": 0,
        "print_width": None,
        "read_only": 0,
        "read_only_depends_on": None,
        "report_hide": 0,
        "reqd": 0,
        "search_index": 0,
        "translatable": 1,
        "unique": 0,
        "width": None
        },
        {
        "_assign": None,
        "_comments": None,
        "_liked_by": None,
        "_user_tags": None,
        "allow_in_quick_entry": 0,
        "allow_on_submit": 0,
        "bold": 0,
        "collapsible": 0,
        "collapsible_depends_on": None,
        "columns": 0,
        "creation": "2024-05-01 09:51:19.454292",
        "default": None,
        "depends_on": None,
        "description": None,
        "docstatus": 0,
        "dt": "Sales Invoice",
        "fetch_from": None,
        "fetch_if_empty": 0,
        "fieldname": "icv",
        "fieldtype": "Data",
        "hidden": 0,
        "hide_border": 0,
        "hide_days": 0,
        "hide_seconds": 0,
        "idx": 210,
        "ignore_user_permissions": 0,
        "ignore_xss_filter": 0,
        "in_global_search": 0,
        "in_list_view": 0,
        "in_preview": 0,
        "in_standard_filter": 0,
        "insert_after": "zatca_status",
        "is_system_generated": 0,
        "is_virtual": 0,
        "label": "ICV",
        "length": 0,
        "mandatory_depends_on": None,
        "modified": "2024-05-01 09:52:24.705598",
        "modified_by": "Administrator",
        "module": None,
        "name": "Sales Invoice-custom_icv",
        "no_copy": 0,
        "non_negative": 0,
        "options": None,
        "owner": "Administrator",
        "permlevel": 0,
        "precision": "",
        "print_hide": 0,
        "print_hide_if_no_value": 0,
        "print_width": None,
        "read_only": 0,
        "read_only_depends_on": None,
        "report_hide": 0,
        "reqd": 0,
        "search_index": 0,
        "translatable": 0,
        "unique": 0,
        "width": None
        },
        {
        "_assign": None,
        "_comments": None,
        "_liked_by": None,
        "_user_tags": None,
        "allow_in_quick_entry": 0,
        "allow_on_submit": 0,
        "bold": 0,
        "collapsible": 0,
        "collapsible_depends_on": None,
        "columns": 0,
        "creation": "2024-05-01 13:11:56.294669",
        "default": None,
        "depends_on": None,
        "description": None,
        "docstatus": 0,
        "dt": "Sales Invoice",
        "fetch_from": None,
        "fetch_if_empty": 0,
        "fieldname": "hash_qr",
        "fieldtype": "Long Text",
        "hidden": 0,
        "hide_border": 0,
        "hide_days": 0,
        "hide_seconds": 0,
        "idx": 211,
        "ignore_user_permissions": 0,
        "ignore_xss_filter": 0,
        "in_global_search": 0,
        "in_list_view": 0,
        "in_preview": 0,
        "in_standard_filter": 0,
        "insert_after": "icv",
        "is_system_generated": 0,
        "is_virtual": 0,
        "label": "Hash qr",
        "length": 0,
        "mandatory_depends_on": "",
        "modified": "2024-05-01 13:44:30.991618",
        "modified_by": "Administrator",
        "module": None,
        "name": "Sales Invoice-custom_hash_qr",
        "no_copy": 0,
        "non_negative": 0,
        "options": None,
        "owner": "Administrator",
        "permlevel": 0,
        "precision": "",
        "print_hide": 0,
        "print_hide_if_no_value": 0,
        "print_width": None,
        "read_only": 1,
        "read_only_depends_on": None,
        "report_hide": 0,
        "reqd": 0,
        "search_index": 0,
        "translatable": 0,
        "unique": 0,
        "width": None
        },
        {
        "_assign": None,
        "_comments": None,
        "_liked_by": None,
        "_user_tags": None,
        "allow_in_quick_entry": 0,
        "allow_on_submit": 0,
        "bold": 0,
        "collapsible": 0,
        "collapsible_depends_on": None,
        "columns": 0,
        "creation": "2024-04-29 12:47:10.528380",
        "default": None,
        "depends_on": None,
        "description": None,
        "docstatus": 0,
        "dt": "Sales Invoice",
        "fetch_from": "customer.bill_type",
        "fetch_if_empty": 0,
        "fieldname": "bill_type",
        "fieldtype": "Select",
        "hidden": 0,
        "hide_border": 0,
        "hide_days": 0,
        "hide_seconds": 0,
        "idx": 6,
        "ignore_user_permissions": 0,
        "ignore_xss_filter": 0,
        "in_global_search": 0,
        "in_list_view": 0,
        "in_preview": 0,
        "in_standard_filter": 0,
        "insert_after": "customer",
        "is_system_generated": 0,
        "is_virtual": 0,
        "label": "Bill Type",
        "length": 0,
        "mandatory_depends_on": None,
        "modified": "2024-05-02 08:38:07.981400",
        "modified_by": "Administrator",
        "module": None,
        "name": "Sales Invoice-custom_bill_type",
        "no_copy": 0,
        "non_negative": 0,
        "options": "\nB2B\nB2C",
        "owner": "Administrator",
        "permlevel": 0,
        "precision": "",
        "print_hide": 0,
        "print_hide_if_no_value": 0,
        "print_width": None,
        "read_only": 0,
        "read_only_depends_on": None,
        "report_hide": 0,
        "reqd": 0,
        "search_index": 0,
        "translatable": 0,
        "unique": 0,
        "width": None
        },
        {
        "_assign": None,
        "_comments": None,
        "_liked_by": None,
        "_user_tags": None,
        "allow_in_quick_entry": 0,
        "allow_on_submit": 0,
        "bold": 0,
        "collapsible": 0,
        "collapsible_depends_on": None,
        "columns": 0,
        "creation": "2024-05-20 11:15:34.053850",
        "default": None,
        "depends_on": None,
        "description": None,
        "docstatus": 0,
        "dt": "Sales Invoice",
        "fetch_from": None,
        "fetch_if_empty": 0,
        "fieldname": "custom_column_break_u2l8b",
        "fieldtype": "Column Break",
        "hidden": 0,
        "hide_border": 0,
        "hide_days": 0,
        "hide_seconds": 0,
        "idx": 212,
        "ignore_user_permissions": 0,
        "ignore_xss_filter": 0,
        "in_global_search": 0,
        "in_list_view": 0,
        "in_preview": 0,
        "in_standard_filter": 0,
        "insert_after": "hash_qr",
        "is_system_generated": 0,
        "is_virtual": 0,
        "label": None,
        "length": 0,
        "mandatory_depends_on": None,
        "modified": "2024-05-20 11:15:34.053850",
        "modified_by": "Administrator",
        "module": None,
        "name": "Sales Invoice-custom_column_break_u2l8b",
        "no_copy": 0,
        "non_negative": 0,
        "options": None,
        "owner": "Administrator",
        "permlevel": 0,
        "precision": "",
        "print_hide": 0,
        "print_hide_if_no_value": 0,
        "print_width": None,
        "read_only": 0,
        "read_only_depends_on": None,
        "report_hide": 0,
        "reqd": 0,
        "search_index": 0,
        "translatable": 0,
        "unique": 0,
        "width": None
        },
        {
        "_assign": None,
        "_comments": None,
        "_liked_by": None,
        "_user_tags": None,
        "allow_in_quick_entry": 0,
        "allow_on_submit": 0,
        "bold": 0,
        "collapsible": 0,
        "collapsible_depends_on": None,
        "columns": 0,
        "creation": "2024-05-20 11:15:35.158776",
        "default": None,
        "depends_on": None,
        "description": None,
        "docstatus": 0,
        "dt": "Sales Invoice",
        "fetch_from": None,
        "fetch_if_empty": 0,
        "fieldname": "zatca_additional",
        "fieldtype": "Float",
        "hidden": 0,
        "hide_border": 0,
        "hide_days": 0,
        "hide_seconds": 0,
        "idx": 215,
        "ignore_user_permissions": 0,
        "ignore_xss_filter": 0,
        "in_global_search": 0,
        "in_list_view": 0,
        "in_preview": 0,
        "in_standard_filter": 0,
        "insert_after": "zatca_discount",
        "is_system_generated": 0,
        "is_virtual": 0,
        "label": "Zatca Additional",
        "length": 0,
        "mandatory_depends_on": None,
        "modified": "2024-05-20 11:28:39.449643",
        "modified_by": "Administrator",
        "module": None,
        "name": "Sales Invoice-custom_zatca_additional",
        "no_copy": 0,
        "non_negative": 0,
        "options": None,
        "owner": "Administrator",
        "permlevel": 0,
        "precision": "",
        "print_hide": 0,
        "print_hide_if_no_value": 0,
        "print_width": None,
        "read_only": 0,
        "read_only_depends_on": None,
        "report_hide": 0,
        "reqd": 0,
        "search_index": 0,
        "translatable": 0,
        "unique": 0,
        "width": None
        },
        {
        "_assign": None,
        "_comments": None,
        "_liked_by": None,
        "_user_tags": None,
        "allow_in_quick_entry": 0,
        "allow_on_submit": 0,
        "bold": 0,
        "collapsible": 0,
        "collapsible_depends_on": None,
        "columns": 0,
        "creation": "2024-05-20 11:15:34.471245",
        "default": None,
        "depends_on": None,
        "description": None,
        "docstatus": 0,
        "dt": "Sales Invoice",
        "fetch_from": None,
        "fetch_if_empty": 0,
        "fieldname": "zatca_discount",
        "fieldtype": "Float",
        "hidden": 0,
        "hide_border": 0,
        "hide_days": 0,
        "hide_seconds": 0,
        "idx": 214,
        "ignore_user_permissions": 0,
        "ignore_xss_filter": 0,
        "in_global_search": 0,
        "in_list_view": 0,
        "in_preview": 0,
        "in_standard_filter": 0,
        "insert_after": "zatca_taxamount",
        "is_system_generated": 0,
        "is_virtual": 0,
        "label": "Zatca Discount",
        "length": 0,
        "mandatory_depends_on": None,
        "modified": "2024-05-20 11:59:07.295138",
        "modified_by": "Administrator",
        "module": None,
        "name": "Sales Invoice-custom_zatca_discount",
        "no_copy": 0,
        "non_negative": 0,
        "options": None,
        "owner": "Administrator",
        "permlevel": 0,
        "precision": "",
        "print_hide": 0,
        "print_hide_if_no_value": 0,
        "print_width": None,
        "read_only": 0,
        "read_only_depends_on": None,
        "report_hide": 0,
        "reqd": 0,
        "search_index": 0,
        "translatable": 0,
        "unique": 0,
        "width": None
        },
        {
        "_assign": None,
        "_comments": None,
        "_liked_by": None,
        "_user_tags": None,
        "allow_in_quick_entry": 0,
        "allow_on_submit": 0,
        "bold": 0,
        "collapsible": 0,
        "collapsible_depends_on": None,
        "columns": 0,
        "creation": "2024-05-20 11:58:17.955861",
        "default": None,
        "depends_on": None,
        "description": None,
        "docstatus": 0,
        "dt": "Sales Invoice",
        "fetch_from": None,
        "fetch_if_empty": 0,
        "fieldname": "zatca_taxamount",
        "fieldtype": "Float",
        "hidden": 0,
        "hide_border": 0,
        "hide_days": 0,
        "hide_seconds": 0,
        "idx": 213,
        "ignore_user_permissions": 0,
        "ignore_xss_filter": 0,
        "in_global_search": 0,
        "in_list_view": 0,
        "in_preview": 0,
        "in_standard_filter": 0,
        "insert_after": "custom_column_break_u2l8b",
        "is_system_generated": 0,
        "is_virtual": 0,
        "label": "Zatca Tax Amount",
        "length": 0,
        "mandatory_depends_on": None,
        "modified": "2024-05-20 11:59:54.449249",
        "modified_by": "Administrator",
        "module": None,
        "name": "Sales Invoice-custom_zatca_taxamount",
        "no_copy": 0,
        "non_negative": 0,
        "options": None,
        "owner": "Administrator",
        "permlevel": 0,
        "precision": "",
        "print_hide": 0,
        "print_hide_if_no_value": 0,
        "print_width": None,
        "read_only": 0,
        "read_only_depends_on": None,
        "report_hide": 0,
        "reqd": 0,
        "search_index": 0,
        "translatable": 0,
        "unique": 0,
        "width": None
        },
        {
        "_assign": None,
        "_comments": None,
        "_liked_by": None,
        "_user_tags": None,
        "allow_in_quick_entry": 0,
        "allow_on_submit": 0,
        "bold": 0,
        "collapsible": 0,
        "collapsible_depends_on": None,
        "columns": 0,
        "creation": "2024-05-27 12:19:42.033529",
        "default": None,
        "depends_on": None,
        "description": None,
        "docstatus": 0,
        "dt": "Sales Invoice",
        "fetch_from": None,
        "fetch_if_empty": 0,
        "fieldname": "zakat_",
        "fieldtype": "Section Break",
        "hidden": 0,
        "hide_border": 0,
        "hide_days": 0,
        "hide_seconds": 0,
        "idx": 167,
        "ignore_user_permissions": 0,
        "ignore_xss_filter": 0,
        "in_global_search": 0,
        "in_list_view": 0,
        "in_preview": 0,
        "in_standard_filter": 0,
        "insert_after": "more_info_tab",
        "is_system_generated": 0,
        "is_virtual": 0,
        "label": "Zakat ",
        "length": 0,
        "mandatory_depends_on": None,
        "modified": "2024-05-27 12:19:42.033529",
        "modified_by": "zakat@co.com",
        "module": None,
        "name": "Sales Invoice-zakat_",
        "no_copy": 0,
        "non_negative": 0,
        "options": None,
        "owner": "zakat@co.com",
        "permlevel": 0,
        "precision": "",
        "print_hide": 0,
        "print_hide_if_no_value": 0,
        "print_width": None,
        "read_only": 0,
        "read_only_depends_on": None,
        "report_hide": 0,
        "reqd": 0,
        "search_index": 0,
        "translatable": 0,
        "unique": 0,
        "width": None
        },
        {
        "_assign": None,
        "_comments": None,
        "_liked_by": None,
        "_user_tags": None,
        "allow_in_quick_entry": 0,
        "allow_on_submit": 0,
        "bold": 0,
        "collapsible": 0,
        "collapsible_depends_on": None,
        "columns": 0,
        "creation": "2024-05-27 12:53:31.143739",
        "default": None,
        "depends_on": None,
        "description": None,
        "docstatus": 0,
        "dt": "Sales Invoice",
        "fetch_from": None,
        "fetch_if_empty": 0,
        "fieldname": "delivery_date",
        "fieldtype": "Date",
        "hidden": 0,
        "hide_border": 0,
        "hide_days": 0,
        "hide_seconds": 0,
        "idx": 17,
        "ignore_user_permissions": 0,
        "ignore_xss_filter": 0,
        "in_global_search": 0,
        "in_list_view": 0,
        "in_preview": 0,
        "in_standard_filter": 0,
        "insert_after": "due_date",
        "is_system_generated": 0,
        "is_virtual": 0,
        "label": "Delivery Date",
        "length": 0,
        "mandatory_depends_on": None,
        "modified": "2024-05-27 12:53:31.143739",
        "modified_by": "Administrator",
        "module": None,
        "name": "Sales Invoice-delivery_date",
        "no_copy": 0,
        "non_negative": 0,
        "options": None,
        "owner": "Administrator",
        "permlevel": 0,
        "precision": "",
        "print_hide": 0,
        "print_hide_if_no_value": 0,
        "print_width": None,
        "read_only": 0,
        "read_only_depends_on": None,
        "report_hide": 0,
        "reqd": 0,
        "search_index": 0,
        "translatable": 0,
        "unique": 0,
        "width": None
        },
       
  
    { "_assign": None,
   "_comments": None,
   "_liked_by": None,
   "_user_tags": None,
   "allow_in_quick_entry": 0,
   "allow_on_submit": 0,
   "bold": 0,
   "collapsible": 0,
   "collapsible_depends_on": None,
   "columns": 0,
   "creation": "2024-06-06 11:09:11.477714",
   "default": None,
   "depends_on": None,
   "description": None,
   "docstatus": 0,
   "dt": "Sales Invoice Item",
   "fetch_from": None,
   "fetch_if_empty": 0,
   "fieldname": "vat_category_reason",
   "fieldtype": "Data",
   "hidden": 0,
   "hide_border": 0,
   "hide_days": 0,
   "hide_seconds": 0,
   "idx": 52,
   "ignore_user_permissions": 0,
   "ignore_xss_filter": 0,
   "in_global_search": 0,
   "in_list_view": 0,
   "in_preview": 0,
   "in_standard_filter": 0,
   "insert_after": "accounting",
   "is_system_generated": 0,
   "is_virtual": 0,
   "label": "VAT category Reasons",
   "length": 0,
   "mandatory_depends_on": None,
   "modified": "2024-06-06 11:09:11.477714",
   "modified_by": "Administrator",
   "module": None,
   "name": "Sales Invoice Item-vat_category",
   "no_copy": 0,
   "non_negative": 0,
   "options":None,
   "owner": "Administrator",
   "permlevel": 0,
   "precision": "",
   "print_hide": 0,
   "print_hide_if_no_value": 0,
   "print_width": None,
   "read_only": 0,
   "read_only_depends_on": None,
   "report_hide": 0,
   "reqd": 0,
   "search_index": 0,
   "translatable": 0,
   "unique": 0,
   "width": None
  },  
  {
    "_assign": None,
    "_comments": None,
    "_liked_by": None,
    "_user_tags": None,
    "allow_in_quick_entry": 0,
    "allow_on_submit": 0,
    "bold": 0,
    "collapsible": 0,
    "collapsible_depends_on": None,
    "columns": 0,
    "creation": "2024-06-06 11:09:11.477714",
    "default": None,
    "depends_on": None,
    "description": None,
    "docstatus": 0,
    "dt": "Sales Invoice Item",
    "fetch_from": None,
    "fetch_if_empty": 0,
    "fieldname": "vat_exemption_reason_code",
    "fieldtype": "Data",
    "hidden": 0,
    "hide_border": 0,
    "hide_days": 0,
    "hide_seconds": 0,
    "idx": 52,
    "ignore_user_permissions": 0,
    "ignore_xss_filter": 0,
    "in_global_search": 0,
    "in_list_view": 0,
    "in_preview": 0,
    "in_standard_filter": 0,
    "insert_after": "vat_category",
    "is_system_generated": 0,
    "is_virtual": 0,
    "label": "VAT exemption reason code",
    "length": 0,
    "mandatory_depends_on": None,
    "modified": "2024-06-06 11:09:11.477714",
    "modified_by": "Administrator",
    "module": None,
    "name": "Sales Invoice Item-vat_category",
    "no_copy": 0,
    "non_negative": 0,
    "options": None,
    "owner": "Administrator",
    "permlevel": 0,
    "precision": "",
    "print_hide": 0,
    "print_hide_if_no_value": 0,
    "print_width": None,
    "read_only": 1,
    "read_only_depends_on": None,
    "report_hide": 0,
    "reqd": 0,
    "search_index": 0,
    "translatable": 0,
    "unique": 0,
    "width": None,
   }, 
   {
    "_assign": None,
    "_comments": None,
    "_liked_by": None,
    "_user_tags": None,
    "allow_in_quick_entry": 0,
    "allow_on_submit": 0,
    "bold": 0,
    "collapsible": 0,
    "collapsible_depends_on": None,
    "columns": 0,
    "creation": "2024-06-06 11:09:11.477714",
    "default": None,
    "depends_on": None,
    "description": None,
    "docstatus": 0,
    "dt": "Sales Invoice Item",
    "fetch_from": None,
    "fetch_if_empty": 0,
    "fieldname": "vat_category_code",
    "fieldtype": "Select",
    "hidden": 0,
    "hide_border": 0,
    "hide_days": 0,
    "hide_seconds": 0,
    "idx": 52,
    "ignore_user_permissions": 0,
    "ignore_xss_filter": 0,
    "in_global_search": 0,
    "in_list_view": 0,
    "in_preview": 0,
    "in_standard_filter": 0,
    "insert_after": "vat_exemption_reason_code",
    "is_system_generated": 0,
    "is_virtual": 0,
    "label": "VAT category code",
    "length": 0,
    "mandatory_depends_on": None,
    "modified": "2024-06-06 11:09:11.477714",
    "modified_by": "Administrator",
    "module": None,
    "name": "Sales Invoice Item-vat_category",
    "no_copy": 0,
    "non_negative": 0,
    "options": "\nR\nZ",
    "owner": "Administrator",
    "permlevel": 0,
    "precision": "",
    "print_hide": 0,
    "print_hide_if_no_value": 0,
    "print_width": None,
    "read_only": 1,
    "read_only_depends_on": None,
    "report_hide": 0,
    "reqd": 0,
    "search_index": 0,
    "translatable": 0,
    "unique": 0,
    "width": None
   }
    ]
    return  custom_fields

    
