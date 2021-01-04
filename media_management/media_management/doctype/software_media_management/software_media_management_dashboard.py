from __future__ import unicode_literals

from frappe import _


def get_data():
	return {
		'fieldname': 'reference_name',
        'non_standard_fieldnames': {
            'Event': 'reference_docname',
            'Website_Link_media_management': 'link_name'
        },
        # 'internal_links': {
		# 	'Website_Link_media_management': ['links', 'link_name'],
        # },
		'transactions': [
            {
				'label': _('Note'),
				'items': ['Note']
			},
            {
				'label': _('ToDo'),
				'items': ['ToDo']
			},
			{
				'label': _('Event'),
				'items': ['Event']
			},
			{
				'label': _('Website Link'),
				'items': ['Website_Link_media_management']
			}
		]
	}
