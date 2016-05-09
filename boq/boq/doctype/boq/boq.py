# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc


form_grid_templates = {
	"items": "templates/form_grid/boq_grid.html"
}

class Boq(Document):
	pass

@frappe.whitelist()
def make_quotation(source_name, target_doc=None):
	doclist = get_mapped_doc("Boq", source_name, {
		"Boq": {
			"doctype": "Quotation",
			"field_map": {
				"account_manager": "tablix_rep",
				"name": "enq_no",
			}
		},
		"Boq Item": {
			"doctype": "Quotation Item",
			"field_map": {
				
				"uom": "stock_uom",
				"selling_price": "rate",
				"sale_amount": "total",
			}
		}
	})

	return doclist
