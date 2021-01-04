frappe.ui.form.on("Event", {

	refresh: function (frm) {

        if (frm.doc.__islocal) {
			const last_doc = frappe.contacts.get_last_doc(frm);
			frm.set_value('event_participants', '');

			frm.add_child('event_participants', {
				reference_doctype: last_doc.doctype,
				reference_docname: last_doc.docname, 
			});
		}

		frm.refresh_field("event_participants");
        
	},
});