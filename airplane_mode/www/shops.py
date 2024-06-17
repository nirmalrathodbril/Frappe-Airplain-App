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
	return context
