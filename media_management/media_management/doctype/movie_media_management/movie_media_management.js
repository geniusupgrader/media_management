// Copyright (c) 2020, Robin Rosenstock and contributors
// For license information, please see license.txt

frappe.ui.form.on('Movie_media_management', {
	refresh(frm) {
	frm.add_custom_button(__("Open Trailer"), function() {
		window.open(frm.doc.trailer);
	});
	}
})
