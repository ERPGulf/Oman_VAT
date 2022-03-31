from . import __version__ as app_version

app_name = "oman_vat"
app_title = "OMAN VAT"
app_publisher = "ERPGulf"
app_description = "OMAN VAT Management and Reporting"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "support@erpgulf.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/oman_vat/css/oman_vat.css"
# app_include_js = "/assets/oman_vat/js/oman_vat.js"

# include js, css files in header of web template
# web_include_css = "/assets/oman_vat/css/oman_vat.css"
# web_include_js = "/assets/oman_vat/js/oman_vat.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "oman_vat/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "oman_vat.install.before_install"
# after_install = "oman_vat.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "oman_vat.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    "Company": {
        "on_update": "oman_vat.oman_vat.setup.operations.setup_oman_vat_setting.create_oman_vat_setting",
        "on_update": "oman_vat.oman_vat.setup.operations.setup_oman_vat_setting.make_custom_fields"
    },
    "Sales Invoice": {
        "after_insert": "oman_vat.events.accounts.sales_invoice.create_qr_code",
        "on_trash": "oman_vat.events.accounts.sales_invoice.delete_qr_code_file"
    }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"oman_vat.tasks.all"
# 	],
# 	"daily": [
# 		"oman_vat.tasks.daily"
# 	],
# 	"hourly": [
# 		"oman_vat.tasks.hourly"
# 	],
# 	"weekly": [
# 		"oman_vat.tasks.weekly"
# 	]
# 	"monthly": [
# 		"oman_vat.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "oman_vat.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "oman_vat.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "oman_vat.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
    {
        "doctype": "{doctype_1}",
        "filter_by": "{filter_by}",
        "redact_fields": ["{field_1}", "{field_2}"],
        "partial": 1,
    },
    {
        "doctype": "{doctype_2}",
        "filter_by": "{filter_by}",
        "partial": 1,
    },
    {
        "doctype": "{doctype_3}",
        "strict": False,
    },
    {
        "doctype": "{doctype_4}"
    }
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"oman_vat.auth.validate"
# ]

fixtures = [
    {
        'dt': 'Custom Field',
        'filters': {
            'name': ['in', [
                'Sales Invoice-qr_code',
                'Company-company_name_in_arabic',
                'Address-address_in_arabic',
                'Customer-arabic_name',
                'Contact-is_billing_contact'
            ]]
        }
    }
]

jenv = {
    'methods': [
        'string_to_json:oman_vat.jinja.utils.string_to_json'
    ]
}
