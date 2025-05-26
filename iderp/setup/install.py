import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def after_install():
    """Create custom fields required by the iderp app."""
    custom_fields = {
        "Item": [
            dict(fieldname="product_type", label="Product Type", fieldtype="Select",
                 options="Per Square Meter\nPer Piece\nPer Linear Meter\nClothing", insert_after="item_name"),
        ],
        "Quotation Item": [
            dict(fieldname="width", label="Width", fieldtype="Float", insert_after="qty"),
            dict(fieldname="height", label="Height", fieldtype="Float", insert_after="width"),
            dict(fieldname="length", label="Length", fieldtype="Float", insert_after="height"),
            dict(fieldname="size", label="Size", fieldtype="Data", insert_after="length"),
            dict(fieldname="color", label="Color", fieldtype="Data", insert_after="size"),
            dict(fieldname="customization_type", label="Customization Type", fieldtype="Data", insert_after="color"),
            dict(fieldname="product_type", label="Product Type", fieldtype="Select",
                 options="Per Square Meter\nPer Piece\nPer Linear Meter\nClothing", insert_after="customization_type"),
        ],
        "Sales Order Item": [
            dict(fieldname="width", label="Width", fieldtype="Float", insert_after="qty"),
            dict(fieldname="height", label="Height", fieldtype="Float", insert_after="width"),
            dict(fieldname="length", label="Length", fieldtype="Float", insert_after="height"),
            dict(fieldname="size", label="Size", fieldtype="Data", insert_after="length"),
            dict(fieldname="color", label="Color", fieldtype="Data", insert_after="size"),
            dict(fieldname="customization_type", label="Customization Type", fieldtype="Data", insert_after="color"),
            dict(fieldname="product_type", label="Product Type", fieldtype="Select",
                 options="Per Square Meter\nPer Piece\nPer Linear Meter\nClothing", insert_after="customization_type"),
        ],
        "Sales Invoice Item": [
            dict(fieldname="width", label="Width", fieldtype="Float", insert_after="qty"),
            dict(fieldname="height", label="Height", fieldtype="Float", insert_after="width"),
            dict(fieldname="length", label="Length", fieldtype="Float", insert_after="height"),
            dict(fieldname="size", label="Size", fieldtype="Data", insert_after="length"),
            dict(fieldname="color", label="Color", fieldtype="Data", insert_after="size"),
            dict(fieldname="customization_type", label="Customization Type", fieldtype="Data", insert_after="color"),
            dict(fieldname="product_type", label="Product Type", fieldtype="Select",
                 options="Per Square Meter\nPer Piece\nPer Linear Meter\nClothing", insert_after="customization_type"),
        ],
    }
    create_custom_fields(custom_fields, update=True)
