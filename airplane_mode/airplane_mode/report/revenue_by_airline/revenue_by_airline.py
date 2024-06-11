# Copyright (c) 2024, Nirmal Rathod and contributors
# For license information, please see license.txt


import frappe


def execute(filters=None):
	print("============================= REPORT")
	columns = [
		{
			"fieldName": "airline",
			"label": "Airline",
			"fieldtype": "data"
		},
		{
			"fieldName": "total_revenue",
			"label": "Total Revenue",
			"fieldtype": "Currency",
			"Options": "AED"
		}
	]
	data = get_airline_revenue()
	return columns, data


def get_airline_revenue():
    # Fetch all airlines
    airlines = frappe.get_all('Airline', fields=['name'])

    data = []

    for airline in airlines:
        # Fetch total revenue for each airline
        revenue = frappe.db.sql("""
            SELECT SUM(at.flight_price) as total_revenue
            FROM `tabAirplane Ticket` at
            JOIN `tabAirplane Flight` af ON at.flight = af.name
            JOIN `tabAirplane` a ON af.airplane = a.name
            WHERE a.airline = %s
        """, (airline['name'],), as_list=True)

        # Ensure that the result is valid
        total_revenue = revenue[0][0] if revenue and revenue[0][0] is not None else 0

        # Append the result to data list
        data.append({
            "airline": airline['name'],
            "total_revenue": total_revenue
        })

    return data
