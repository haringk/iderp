import frappe
from erpnext.selling.doctype.quotation.quotation import make_sales_order as _make_sales_order
from erpnext.selling.doctype.sales_order.sales_order import make_sales_invoice as _make_sales_invoice
from iderp.utils.discounts import copy_item_fields


def make_sales_order(source_name, target_doc=None):
    """Create a Sales Order from Quotation and copy custom item fields."""
    so = _make_sales_order(source_name, target_doc)
    quotation = frappe.get_doc("Quotation", source_name)
    for q_item, so_item in zip(quotation.items, so.items):
        copy_item_fields(q_item, so_item)
    return so


def make_sales_invoice(source_name, target_doc=None):
    """Create a Sales Invoice from Sales Order and copy custom item fields."""
    si = _make_sales_invoice(source_name, target_doc)
    sales_order = frappe.get_doc("Sales Order", source_name)
    for so_item, si_item in zip(sales_order.items, si.items):
        copy_item_fields(so_item, si_item)
    return si
