// Copyright (c) 2020, Robin Rosenstock and contributors
// For license information, please see license.txt

frappe.ui.form.on('Book_media_management', {
	refresh(frm) {
		cur_frm.doc.book_title_read_only = cur_frm.doc.name1
	}
})
