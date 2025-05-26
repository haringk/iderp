import frappe

CUSTOM_ITEM_FIELDS = [
    "width",
    "height",
    "length",
    "size",
    "color",
    "personalization_type",
]


def copy_custom_fields(source_doc, target_doc):
    """Copy custom item fields from source to target document."""
    if not (hasattr(source_doc, "items") and hasattr(target_doc, "items")):
        return
    for src_item, tgt_item in zip(source_doc.items, target_doc.items):
        for field in CUSTOM_ITEM_FIELDS:
            if src_item.get(field) is not None:
                tgt_item.set(field, src_item.get(field))
