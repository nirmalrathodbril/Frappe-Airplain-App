# Copyright (c) 2024, Nirmal Rathod and contributors
# For license information, please see license.txt
import frappe
# import frappe
from frappe.model.document import Document


class RentPayment(Document):
	pass

	def send_rent_reminders(self):
		if frappe.db.get_single_value('Global Configuration', 'enable_rent_reminders'):
			contracts = frappe.get_all('Contract', filters={'end_date': ('>', frappe.utils.nowdate())})
			for contract in contracts:
				tenant = frappe.get_doc('Tenant', contract.tenant)
				frappe.sendmail(
					recipients=tenant.email,
					subject='Rent Reminder',
					message='Your rent is due. Please make the payment.'
				)

