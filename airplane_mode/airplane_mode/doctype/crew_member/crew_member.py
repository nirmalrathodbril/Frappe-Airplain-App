# Copyright (c) 2024, Nirmal Rathod and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class CrewMember(Document):

	def before_save(self):
		fn = self.first_name if self.first_name is not None else ""
		ln = self.last_name if self.last_name is not None else ""
		if ln != "":
			self.full_name = f"{fn} {ln}"
		else:
			self.full_name = f"{fn}"
