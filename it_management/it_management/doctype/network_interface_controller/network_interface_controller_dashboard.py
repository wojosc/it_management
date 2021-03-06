from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		'fieldname': 'network_interface_controller',
		'transactions': [
      {
				'label': _('Network'),
				'items': ['IP Address']
			},
      {
				'label': _('VLAN'),
				'items': []
			},
      {
				'label': _('Configuration Item Host'),
				'items': ['Configuration Item']
			},
		]
}
