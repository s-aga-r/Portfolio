// Copyright (c) 2022, Sagar Sharma and contributors
// For license information, please see license.txt

frappe.ui.form.on('Portfolio', {
	setup: function (frm) {
		frm.set_query("folder", "items", () => {
			return {
				filters: {
					is_folder: 1,
					is_private: 0
				}
			};
		});
	}
});
