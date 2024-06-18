# Copyright (c) 2024, Nirmal Rathod and contributors
# For license information, please see license.txt
import frappe
# import frappe
from frappe.model.document import Document


class RentPayment(Document):
	pass

	def send_rent_reminders(self):
		print("send rent reminder started")



		if frappe.db.get_single_value('Global Configuration', 'enable_rent_reminders'):
			contracts = frappe.get_all('Contract', filters={'end_date': ('>', frappe.utils.nowdate())})
			print(contracts)
			for contract in contracts:
				# create a rent payment doc type with

				tenant = frappe.get_doc('Tenant', contract.tenant)
				print(tenant)
				frappe.sendmail(
					recipients=tenant.email,
					subject='Rent Reminder',
					message='Your rent is due. Please make the payment.'
				)

		print("send rent reminder ENDED")
