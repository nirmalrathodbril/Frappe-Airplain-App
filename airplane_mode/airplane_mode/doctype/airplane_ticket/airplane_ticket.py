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


	def validation_to_check(self):
		print("before submit from Airplate ticket")
		if (self.status != 'Boarded'):
			frappe.throw("Ticket can not be submit as Flight has not been boarded yet.")


	def before_save(self):
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
		self.seat = f"{number}{letter}"
