app_name = "iderp"
app_title = "iderp"
app_publisher = "idstudio AI"
app_description = "Custom app for ERPNext"
app_email = "ai@idstudio.org"
app_license = "MIT"


# Hooks
after_install = "iderp.setup.install.after_install"

override_whitelisted_methods = {
    "erpnext.selling.doctype.quotation.quotation.make_sales_order": "iderp.overrides.make_sales_order",
    "erpnext.selling.doctype.sales_order.sales_order.make_sales_invoice": "iderp.overrides.make_sales_invoice",
}

doc_events = {
    "Quotation": {"validate": "iderp.utils.discounts.apply_discounts"},
    "Sales Order": {"validate": "iderp.utils.discounts.apply_discounts"},
    "Sales Invoice": {"validate": "iderp.utils.discounts.apply_discounts"},
}