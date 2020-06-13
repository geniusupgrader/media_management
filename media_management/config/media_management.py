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
              "description": _("Description of Exercise"),
            },
            {
              "type": "doctype",
              "name": "Serie_media_management_zwei",
              "label": _("Serie"),
              "description": _("Description of Exercise"),
            },
            {
              "type": "doctype",
              "name": "Book_media_management_zwei",
              "label": _("Book"),
              "description": _("Description of Exercise"),
            },
            {
              "type": "doctype",
              "name": "Video_media_management",
              "label": _("Video"),
              "description": _("Description of Exercise"),
            },
            {
              "type": "doctype",
              "name": "Game_media_management",
              "label": _("Game"),
              "description": _("Description of Exercise"),
            },
            {
              "type": "doctype",
              "name": "Source_media_management",
              "label": _("Source"),
              "description": _("Description of Exercise"),
            },
            {
              "type": "doctype",
              "name": "Genre_media_management",
              "label": _("Genre"),
              "description": _("Description of Exercise"),
            }
        ]
      }
  ]
