import frappe

no_cache = 1
import frappe


def get_context(context):
	shop_status = frappe.form_dict.get('status')
	airport_code = frappe.form_dict.get('airport_code')

	filters = {}
	if shop_status:
		filters['status'] = shop_status
	if airport_code:
		filters['airport_code'] = airport_code

	context.shops = frappe.get_all('Shop', filters=filters,
								   fields=['shop_no', 'name', 'area', 'tenant', 'airport',
										   'status'])

	context.airports = frappe.get_all('Airport', fields=['code', 'name'], distinct=True)
	context.statuses = ['Unavailable', 'Available', 'Out Of City', 'Discontinue']

	print("======================== FROM Get context")
	print(context.airports)

	#context.airports = [airport['code'] for airport in context.airports]


	return context
