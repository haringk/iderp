import frappe


def get_customer_discount(customer):
    """Return the discount percentage for a customer if defined."""
    if not customer:
        return 0
    discount = frappe.db.get_value("Customer Discount", {"customer": customer}, "discount_percentage")
    return discount or 0


FIELDS = [
    "width",
    "height",
    "length",
    "size",
    "color",
    "customization_type",
    "product_type",
]


def apply_discounts(doc, method=None):
    """Apply quantity and customer discounts to each item."""
    customer_discount = get_customer_discount(getattr(doc, "customer", None))
    for item in getattr(doc, "items", []):
        quantity_discount = calculate_quantity_discount(item)
        total_discount = quantity_discount + customer_discount
        if hasattr(item, "discount_percentage"):
            item.discount_percentage = (item.discount_percentage or 0) + total_discount


def calculate_quantity_discount(item):
    qty = item.qty or 0
    if getattr(item, "product_type", "") == "Per Square Meter":
        qty = (item.width or 0) * (item.height or 0) * qty
    elif getattr(item, "product_type", "") == "Per Linear Meter":
        qty = (item.length or 0) * qty
    # simple example thresholds
    if qty >= 100:
        return 10
    if qty >= 50:
        return 5
    return 0


def copy_item_fields(source_item, target_item):
    for field in FIELDS:
        if hasattr(source_item, field) and hasattr(target_item, field):
            target_item.set(field, source_item.get(field))
