import frappe


def get_context(context):

    result = []

    portfolio_names = frappe.db.get_all("Portfolio", {"is_active": 1})

    if portfolio_names:
        for portfolio_name in portfolio_names:
            portfolio_doc = frappe.get_doc("Portfolio", portfolio_name.get("name"))

            for item in portfolio_doc.get("items"):
                file_names = frappe.db.get_all("File", {"folder": item.get("folder"), "is_folder": 0, "is_private": 0})

                items = []

                for file_name in file_names:
                    items.append(frappe.db.get_value("File", file_name.get("name"), "file_url"))

                result.append(
                    {
                        "category": portfolio_doc.get("category"),
                        "filter": portfolio_doc.get("filter"),
                        "items": items
                    }
                )

    context.data = result

    return context