app_name = "iderp"
app_title = "iderp"
app_publisher = "idstudio AI"
app_description = "Custom app for ERPNext"
app_email = "ai@idstudio.org"
app_license = "MIT"
app_include_js = "/assets/iderp/js/iderp.js"
app_include_css = "/assets/iderp/css/iderp.css"
after_install = "iderp.install.after_install"

doc_events = {
    "Quotation": {
        "on_submit": "iderp.utils.overrides.copy_item_fields"
    },
    "Sales Order": {
        "on_submit": "iderp.utils.overrides.copy_item_fields"
    }
}

