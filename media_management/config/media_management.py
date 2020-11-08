from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
      {
        "label":_("Main Components"),
        "items": [
            {
              "type": "doctype",
              "name": "Movie_media_management",
              "label": _("Movie"),
              "description": _("Description of Exercise"),
            },
            {
              "type": "doctype",
              "name": "Serie_media_management",
              "label": _("Serie"),
              "description": _("Description of Exercise"),
            },
            {
              "type": "doctype",
              "name": "Book_media_management",
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
              "name": "Software_media_management",
              "label": _("Software"),
              "description": _("Description of Software"),
            },     
            {
              "type": "doctype",
              "name": "Image_media_management",
              "label": _("Image"),
              "description": _("Description of Image"),
            },     
            {
              "type": "doctype",
              "name": "Website_Link_media_management",
              "label": _("Website Link"),
              "description": _("Description of Category"),
            }
                    ],
      },
      {
"label":_("Helper Components"),
        "items": [
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
            },
            {
              "type": "doctype",
              "name": "List_media_management",
              "label": _("List"),
              "description": _("Description of Liste"),
            },
            {
              "type": "doctype",
              "name": "Category_media_management",
              "label": _("Category"),
              "description": _("Description of Category"),
            },
            {
              "type": "doctype",
              "name": "License_media_management",
              "label": _("License"),
              "description": _("Description of License"),
            },
            {
              "type": "doctype",
              "name": "Link_collection_media_management",
              "label": _("Link Collection"),
              "description": _("Description of Category"),
            },
            {
              "type": "doctype",
              "name": "Author_media_management",
              "label": _("Author"),
              "description": _("Description of Author"),
            },
            {
              "type": "doctype",
              "name": "Platform_media_management",
              "label": _("Platform"),
              "description": _("Description of Platform"),
            }
        ]


      }
  ]
