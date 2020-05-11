from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
      {
        "label":_("Media Management"),
        "icon": "octicon octicon-briefcase",
        "items": [
                    {
              "type": "doctype",
              "name": "Movie",
              "label": _("Movie"),
              "description": _("Description of Liste"),
            },
      {
        "label":_("Media Management"),
        "icon": "octicon octicon-briefcase",
        "items": [
                    {
              "type": "doctype",
              "name": "Serie",
              "label": _("Serie"),
              "description": _("Description of Liste"),
            },

      {
        "label":_("Media Management"),
        "icon": "octicon octicon-briefcase",
        "items": [
                    {
              "type": "doctype",
              "name": "Staffel",
              "label": _("Staffel"),
              "description": _("Description of Liste"),
            }

        ]
      }
  ]
