"""Utility functions for quantity and customer-based discounts."""

import frappe


def get_customer_discount(customer):
    """Return a discount percentage for the given customer if configured."""
    doc = frappe.get_all(
        "Customer Discount",
        filters={"customer": customer},
        fields=["discount_percentage"],
        limit=1,
    )
    if doc:
        return doc[0].discount_percentage or 0
    return 0


def apply_quantity_discount(quantity, breaks):
    """Return the discount percentage based on quantity breaks."""
    applicable = 0
    for qty, pct in sorted(breaks.items()):
        if quantity >= qty:
            applicable = pct
    return applicable
