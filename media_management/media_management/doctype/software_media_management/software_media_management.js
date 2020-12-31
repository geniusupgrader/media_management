// Copyright (c) 2020, Robin Rosenstock and contributors
// For license information, please see license.txt

frappe.ui.form.on('Software_media_management', {
	before_save(frm) {
		
		var repo = frm.doc.repo
		

		    frappe.call({
            method: "media_management.media_management.doctype.github_settings_media_management.github_settings_media_management.get_github_stars",
            args:{
                githubrepo: repo
            },
            callback: function(r) {
                // console.log(r)
				frm.doc.github_stars = r.message
				frm.doc.github_stars_fetched_date = frappe.datetime.get_today()
            }
        })
		
		frm.refresh()
	}
})