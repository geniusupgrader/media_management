frappe.ui.form.on("ToDo", {

	refresh: function (frm) {

		if (frm.doc.__islocal) {
			const last_doc = frappe.contacts.get_last_doc(frm);
			frm.doc.reference_type = last_doc.doctype
			frm.doc.reference_name = last_doc.docname
			frm.refresh_field("reference_type");
			frm.refresh_field("reference_name");
		}
	},
});