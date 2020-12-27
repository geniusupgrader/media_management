// Copyright (c) 2020, Robin Rosenstock and contributors
// For license information, please see license.txt

frappe.ui.form.on('Serie_media_management', {
	refresh(frm) {
	    
	cur_frm.doc.name_read_only = cur_frm.doc.name1
	
	frm.add_custom_button(__("Open Trailer"), function() {
		window.open(frm.doc.trailer);
	});
	}
})
