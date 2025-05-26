"""Document event handlers to copy custom item fields between transactions."""

import frappe

CUSTOM_FIELDS = [
    "print_width",
    "print_height",
    "print_color"
]


def copy_item_fields(doc, method=None):
    """Copy custom fields from items' previous document."""
    if not getattr(doc, "items", None):
        return
    for item in doc.items:
        if hasattr(item, "prevdoc_docname"):
            src_item = frappe.get_doc(item.prevdoctype + " Item", item.prevdoc_docname)
            for field in CUSTOM_FIELDS:
                if hasattr(src_item, field):
                    item.set(field, getattr(src_item, field))
