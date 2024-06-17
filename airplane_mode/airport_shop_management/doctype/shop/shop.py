# Copyright (c) 2024, Nirmal Rathod and contributors
# For license information, please see license.txt
import frappe
# import frappe
from frappe.model.document import Document


class Shop(Document):
	def validate(self):
		if not self.tenant:
			self.status = 'Available'
		else:
			self.status = 'Occupied'

	@frappe.whitelist()
	def get_available_shops(self):
		return frappe.get_all('Shop', filters={'status': 'Available'})

	@frappe.whitelist()
	def get_occupied_shops(self):
		return frappe.get_all('Shop', filters={'status': 'Leased'})
