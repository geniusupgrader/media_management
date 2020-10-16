# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "media_management"
app_title = "Media Management"
app_publisher = "Robin Rosenstock"
app_description = "Keep an overview over the used Media of yours (Movies, Series, Books, Games)"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "robin.rosenstock@t-online.de"
app_license = "MIT"

# Includes in <head> 
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/media_management/css/media_management.css"
app_include_js = "/assets/js/lead_ext.js"
# app_include_js = "/assets/media_management/js/lead_ext.js"

# include js, css files in header of web template
# web_include_css = "/assets/media_management/css/media_management.css"
# web_include_js = "/assets/media_management/js/media_management.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views

doctype_js = {"Lead" : "public/js/lead_ext2.js"}


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

# Website user home page (by function)
# get_website_user_home_page = "media_management.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "media_management.install.before_install"
# after_install = "media_management.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "media_management.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# doc_events = {
#     "Lead": {
#         "before_save": "media_management.media_management.doctype.website_link_media_management.website_link_media_management.renderlinks"
#     }
# }



# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"media_management.tasks.all"
# 	],
# 	"daily": [
# 		"media_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"media_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"media_management.tasks.weekly"
# 	]
# 	"monthly": [
# 		"media_management.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "media_management.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "media_management.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "media_management.task.get_dashboard_data"
# }

