import frappe
from erpnext.selling.doctype.quotation.quotation import make_sales_order as erp_make_sales_order
from erpnext.selling.doctype.sales_order.sales_order import make_sales_invoice as erp_make_sales_invoice
from .utils.item_utils import copy_custom_fields


def make_sales_order(source_name, target_doc=None):
    doc = erp_make_sales_order(source_name, target_doc)
    source = frappe.get_doc("Quotation", source_name)
    copy_custom_fields(source, doc)
    return doc


def make_sales_invoice(source_name, target_doc=None):
    doc = erp_make_sales_invoice(source_name, target_doc)
    source = frappe.get_doc("Sales Order", source_name)
    copy_custom_fields(source, doc)
    return doc
