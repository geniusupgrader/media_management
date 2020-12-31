# -*- coding: utf-8 -*-
# Copyright (c) 2020, Robin Rosenstock and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import enqueue
import requests
import time

class Github_settings_media_management(Document):

	def validate(self):
		pass



def do_github_query(github_api_key, githubrepo):

	headers = {"Authorization": "Bearer "+github_api_key}

	def run_query(query):
		request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
		if request.status_code == 200:
			return request.json()
		else:
			raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

	query = """
	{{
	resource(url: "{0}") {{
		... on Repository {{
		name
		stargazerCount
		owner {{
			login
		}}
		}}
	}}
	}}
	"""

	query2 = query.format(githubrepo)

	result = run_query(query2) # Execute the query

	try:
		githubstars = result["data"]["resource"]["stargazerCount"]
	except:
		githubstars = -1

	return githubstars



@frappe.whitelist()
def get_github_stars(githubrepo):

	doc = frappe.get_doc('Github_settings_media_management')
	github_api_key = doc.api_github_key

	githubstars = do_github_query(github_api_key, githubrepo)

	return githubstars



@frappe.whitelist()
def update_all_github_stars():
	enqueue(long_job, arg1="arg1", arg2="arg2")



@frappe.whitelist()
def long_job(arg1, arg2):

	frappe.publish_realtime('msgprint', 'Updating all software with latest github stars...')

		# get list of all software where github repo is set
	# all_adresses = frappe.db.get_list("Address", fields=['name'], as_list=True)
	software_list = frappe.db.get_list("Software_media_management", fields=['name'], filters={'repo': ['is', 'set']}, as_list=True)

	for i in software_list:

		software_name = i[0]

		github_repo_url = frappe.db.get_value("Software_media_management", software_name, "repo")

		doc = frappe.get_doc('Github_settings_media_management')
		github_api_key = doc.api_github_key

		print(software_name)

		githubstars = do_github_query(github_api_key, github_repo_url)
		# time.sleep(1)
		print(githubstars)

		frappe.db.set_value("Software_media_management", software_name, "github_stars", githubstars)
		frappe.db.set_value("Software_media_management", software_name, "github_stars_fetched_date", frappe.utils.nowdate())

	frappe.publish_realtime('msgprint', 'Finished updating all software with latest github stars')
