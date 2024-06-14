# Copyright (c) 2024, Nirmal Rathod and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator

# from apps.frappe import frappe


class AirplaneFlight(WebsiteGenerator):

	db_gate = 1;
	def validate(self):
		print("from Validation ")
		db_gate = frappe.db.get_value(self.doctype, self.name, 'gate_no')


	def before_submit(self):
		self.status = "Completed"

	def on_update(self):
		# Check if the gate number has changed
		# print("gate no")
		# print(self.gate_no)
		# print(self.get_db_value('gate_no'))

		#db_gate = frappe.db.get_value(self.doctype, self.name, 'gate_no')


		if self.gate_no != AirplaneFlight.db_gate:
			self.send_gate_change_notification()

	def send_gate_change_notification(self):
		print("calling send_gate_change_notification")

		print(self.as_dict())


		tickets = frappe.get_all('Airplane Ticket', filters={'flight': self.name},
								 fields=['passenger'])

		print("tickets")
		print(tickets)

		for ticket in tickets:
			passenger = frappe.get_doc('Flight Passenger', ticket.passenger)
			print("passenger")
			print(passenger)
			self.send_email_to_passenger(passenger)

	def send_email_to_passenger(self, passenger):
		subject = "Gate Number Changed for Your Flight"
		context = {
			'passenger_name': passenger.full_name,
			# 'flight_no': self.name,
			# 'new_gate_no': self.gate_no,
			# 'airline': self.airline,
			# 'date_time': self.date_time,
			# 'source': self.source,
			# 'destination': self.destination
		}

		print("email template")
		message = "Hello {{ passenger_name }}" #frappe.render_template('path/to/email_template.html', context)
		print(message)

		frappe.sendmail(
			recipients=[passenger.email],
			subject=subject,
			message=message
		)
