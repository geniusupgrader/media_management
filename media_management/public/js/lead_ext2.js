frappe.provide("erpnext.utils");

frappe.ui.form.on('Lead', {
	refresh: function(frm) {
    console.log("hallo3");
    $(cur_frm.fields_dict['website_link_html'].wrapper)
				.html(frappe.render_template("website_links_template",
					cur_frm.doc.__onload))
                    .find(".btn-contact").on("click", function() {
                        frappe.new_doc("Contact");
                    });
	}
});




