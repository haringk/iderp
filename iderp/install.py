"""Installer hooks to create custom fields required by the app."""

import frappe


def after_install():
    # Example: ensure custom fields exist for item dimensions
    create_custom_field(
        doctype="Sales Invoice Item",
        fieldname="print_height",
        fieldtype="Float",
        label="Print Height (cm)"
    )


def create_custom_field(doctype, fieldname, fieldtype, label):
    if not frappe.get_all("Custom Field", filters={"dt": doctype, "fieldname": fieldname}):
        cf = frappe.get_doc({
            "doctype": "Custom Field",
            "dt": doctype,
            "fieldname": fieldname,
            "fieldtype": fieldtype,
            "label": label,
        })
        cf.insert(ignore_permissions=True)
        frappe.db.commit()
