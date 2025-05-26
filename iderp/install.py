import frappe


def after_install():
    """Create custom fields required by the app."""
    from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

    custom_fields = {
        "Item": [
            dict(fieldname="selling_type", fieldtype="Select", label="Selling Type", options="Square Meter\nPiece\nLinear Meter\nClothing"),
            dict(fieldname="default_width", fieldtype="Float", label="Default Width"),
            dict(fieldname="default_height", fieldtype="Float", label="Default Height"),
            dict(fieldname="default_length", fieldtype="Float", label="Default Length"),
            dict(fieldname="default_size", fieldtype="Data", label="Default Size"),
            dict(fieldname="default_color", fieldtype="Data", label="Default Color"),
            dict(fieldname="default_personalization", fieldtype="Data", label="Default Personalization"),
        ],
        "Quotation Item": [
            dict(fieldname="width", fieldtype="Float", label="Width"),
            dict(fieldname="height", fieldtype="Float", label="Height"),
            dict(fieldname="length", fieldtype="Float", label="Length"),
            dict(fieldname="size", fieldtype="Data", label="Size"),
            dict(fieldname="color", fieldtype="Data", label="Color"),
            dict(fieldname="personalization_type", fieldtype="Data", label="Personalization Type"),
        ],
        "Sales Order Item": [
            dict(fieldname="width", fieldtype="Float", label="Width"),
            dict(fieldname="height", fieldtype="Float", label="Height"),
            dict(fieldname="length", fieldtype="Float", label="Length"),
            dict(fieldname="size", fieldtype="Data", label="Size"),
            dict(fieldname="color", fieldtype="Data", label="Color"),
            dict(fieldname="personalization_type", fieldtype="Data", label="Personalization Type"),
        ],
        "Sales Invoice Item": [
            dict(fieldname="width", fieldtype="Float", label="Width"),
            dict(fieldname="height", fieldtype="Float", label="Height"),
            dict(fieldname="length", fieldtype="Float", label="Length"),
            dict(fieldname="size", fieldtype="Data", label="Size"),
            dict(fieldname="color", fieldtype="Data", label="Color"),
            dict(fieldname="personalization_type", fieldtype="Data", label="Personalization Type"),
        ],
    }

    create_custom_fields(custom_fields, update=True)
