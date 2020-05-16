from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
      {
        "label":_("Media Management"),
        "icon": "octicon file-media",
        "items": [
            {
              "type": "doctype",
              "name": "Movie",
              "label": _("Movie"),
              "description": _("Description of Movie"),
            },
            {
              "type": "doctype",
              "name": "Serie",
              "label": _("Serie"),
              "description": _("Description of Serie"),
            },
            {
              "type": "doctype",
              "name": "Book",
              "label": _("Book"),
              "description": _("Description of Book"),
            },
            {
              "type": "doctype",
              "name": "Game",
              "label": _("Game"),
              "description": _("Description of Game"),
            }
        ]
      }
  ]
