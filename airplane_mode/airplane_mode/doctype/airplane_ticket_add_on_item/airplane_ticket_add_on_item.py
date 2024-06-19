# Copyright (c) 2024, Nirmal Rathod and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class AirplaneTicketAddonItem(Document):
	def validate(self):
		print("======== AirplaneTicketAddonItem validate 123")
		add_ons = self.add_ons
		unique_add_ons = list(set(add_ons))
		self.add_ons = unique_add_ons
		print("====================")
		print(self.add_ons)


