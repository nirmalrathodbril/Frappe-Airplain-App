# Copyright (c) 2024, Nirmal Rathod and contributors
# For license information, please see license.txt
import random
import string

import frappe
from frappe.model.document import Document


#from apps.frappe import frappe


class AirplaneTicket(Document):
	def validate(self):
		print("======== AirplaneTicket validate 123")
		add_ons = self.add_ons
		print(add_ons)

		# Dictionary to hold unique add_ons by name
		unique_add_ons_dict = {}
		for add_on in add_ons:
			unique_add_ons_dict[add_on.item] = add_on

		# Update the add_ons with the unique values
		self.add_ons = list(unique_add_ons_dict.values())

		print("====== Result ==============")
		print(self.add_ons)
		self.validation_to_check()

	def validation_to_check(self):
		print("before submit from Airplate ticket")
		if (self.status != 'Boarded'):
			frappe.throw("Ticket can not be submit as Plain has not been boarded yet.")

	def validation_to_available_seats(self):
		# airplane ticket --> airplane flight --> airplane
		print(self.as_dict())
		docFlight = self.flight
		print("Insideeeeee")
		print(docFlight.as_dict())
		docAirplane = frappe.get_doc("Airplane flight", docFlight.flight)
		print(docAirplane.as_dict())
		seatCount = docAirplane.capacity
		print(seatCount)

		# get number of tickets from airplane tickets having seat assigned
		assignedSeatCount = 20

		frappe.throw("Oops, Sold Out!")  # validation_to_available_seats

	def check_seat_availability(self):
		# Fetch the Airplane Flight document
		airplane_flight = frappe.get_doc("Airplane Flight", self.flight)

		# Fetch the Airplane document linked to the Airplane Flight
		airplane = frappe.get_doc("Airplane", airplane_flight.airplane)
		capacity = airplane.capacity

		# Count the existing tickets for the same Airplane Flight
		existing_tickets = frappe.db.count("Airplane Ticket",
										   filters={"flight": self.flight})

		# Check if the new ticket exceeds the capacity
		if existing_tickets >= capacity:
			frappe.throw("Oops, Sold Out!")

	def before_save(self):

		## self.validation_to_available_seats()
		self.check_seat_availability()

		sum_amount = 0
		for item in self.add_ons:
			sum_amount += item.amount

		self.total_amount = sum_amount + self.flight_price

	def on_load(self):
		sum_amount = 0
		for item in self.add_ons:
			sum_amount += item.amount

		self.total_amount = sum_amount + self.flight_price

	def on_submit(self):
		number = random.randint(1, 99)
		# Generate a random uppercase letter
		letter = random.choice(string.ascii_uppercase)
	# Combine number and letter to form seat assignment
	# self.seat = f"{number}{letter}"
