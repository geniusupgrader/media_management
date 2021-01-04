// Copyright (c) 2020, Robin Rosenstock and contributors
// For license information, please see license.txt


frappe.ui.form.on("Website_Link_media_management", {

	before_save: function (frm) {
		frm.doc.link_read_only = "<a href=\"" + frm.doc.link + "\" target=\"_blank\">" + frm.doc.link + "</a>"
	},


	refresh: function (frm) {

		frm.add_custom_button(__("Open Link"), function () {
			window.open(frm.doc.link);
		});


		if (frm.doc.__islocal) {
			const last_doc = frappe.contacts.get_last_doc(frm);
			frm.set_value('links', '');

			var title_field = frappe.get_meta(last_doc.doctype).title_field
			if (title_field) {
				title_field = frappe.model.get_value(last_doc.doctype, last_doc.docname, title_field)
			}
			else {
				title_field = "name"
				title_field = frappe.model.get_value(last_doc.doctype, last_doc.docname, title_field)
			}
			frm.add_child('links', {
				link_doctype: last_doc.doctype,
				link_name: last_doc.docname,
				link_title: title_field
			});
		}

		frm.refresh_field("links");

		if (frm.doc.links) {
			for (let i in frm.doc.links) {
				let link = frm.doc.links[i];
				frm.add_custom_button(__("{0}: {1}", [__(link.link_doctype), __(link.link_name)]), function () {
					frappe.set_route("Form", link.link_doctype, link.link_name);
				}, __("Links"));
			}
		}
	},

});


frappe.ui.form.on("Dynamic Link", {
	link_name: function (frm, cdt, cdn) {
		var child = locals[cdt][cdn];
		if (child.link_name) {
			frappe.model.with_doctype(child.link_doctype, function () {
				var title_field = frappe.get_meta(child.link_doctype).title_field || "name"
				frappe.model.get_value(child.link_doctype, child.link_name, title_field, function (r) {
					frappe.model.set_value(cdt, cdn, "link_title", r[title_field])
				})
			})
		}
	}
})