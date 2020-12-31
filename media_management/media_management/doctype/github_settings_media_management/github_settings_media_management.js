// Copyright (c) 2020, Robin Rosenstock and contributors
// For license information, please see license.txt

// frappe.ui.form.on('Github_settings_media_management', {
// 	// refresh: function(frm) {

// 	// }
// });

frappe.ui.form.on("Github_settings_media_management", {
	refresh: function(frm) {
		frm.add_custom_button(__("Update All Software with Github Repos"), function() {
			
			frappe.call({
			method: "media_management.media_management.doctype.github_settings_media_management.github_settings_media_management.update_all_github_stars",
			callback: function(r) {
				// console.log(r)
				//frm.doc.distance = r.message[0]
				//frm.doc.duration_from_home_address_in_minutes = r.message[1]
				// frm.refresh()
			}
			})
			
		}); 
	}
	});
	


