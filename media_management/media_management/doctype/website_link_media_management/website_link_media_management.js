// Copyright (c) 2020, Robin Rosenstock and contributors
// For license information, please see license.txt

frappe.ui.form.on('Website_Link_media_management', {
	refresh(frm) {
		frm.add_custom_button(__("Open Link"), function() {
		window.open(frm.doc.link);
	});
	frm.doc.link_read_only = frm.doc.link
	}
})

