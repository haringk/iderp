import frappe


def get_quantity_discount(qty: float) -> float:
    """Return discount percentage based on quantity."""
    if qty >= 100:
        return 10.0
    if qty >= 50:
        return 5.0
    return 0.0


def get_customer_discount(customer: str) -> float:
    """Fetch discount percentage for the given customer."""
    return (
        frappe.db.get_value("Customer Discount", {"customer": customer}, "discount_percentage")
        or 0.0
    )


def apply_discounts(doc, method=None):
    """Apply automatic discounts on sales documents."""
    customer_discount = get_customer_discount(doc.customer) if getattr(doc, "customer", None) else 0.0
    for item in getattr(doc, "items", []):
        qty_discount = get_quantity_discount(item.get("qty", 0))
        item.discount_percentage = qty_discount + customer_discount
