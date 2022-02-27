# Copyright (c) 2022, Sagar Sharma and contributors
# For license information, please see license.txt

import re
# import frappe
from frappe.model.document import Document

class Portfolio(Document):
	def validate(self):
		category = re.sub(" +", " ", self.category).lower().lstrip().rstrip()
		self.filter = category.replace(" ", "-")
