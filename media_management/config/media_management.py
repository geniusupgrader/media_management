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
              "name": "Movie_media_management",
              "label": _("Movie"),
              "description": _("Description of Movie"),
            },
            {
              "type": "doctype",
              "name": "Serie_media_management",
              "label": _("Serie"),
              "description": _("Description of Serie"),
            },
            {
              "type": "doctype",
              "name": "Book_media_management",
              "label": _("Book"),
              "description": _("Description of Book"),
            },
            {
              "type": "doctype",
              "name": "Game_media_management",
              "label": _("Game"),
              "description": _("Description of Game"),
            }
        ]
      }
  ]
