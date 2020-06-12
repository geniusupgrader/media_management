from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
      {
        "label":_("Media Management"),
        "items": [
            {
              "type": "doctype",
              "name": "Movie_media_management_zwei",
              "label": _("Movie"),
              "description": _("Description of Movie"),
            }
        ]
      }
  ]
