﻿from openerp import models, fields, api

class sale_order_products_summary(models.Model):
    _inherit = 'sale.order'

    products_summary = fields.Char(compute='_compute_products_summary',string="Résumé des produits", store=False)
    
    @api.one
    @api.onchange('order_line')
    def _compute_products_summary(self):
        cr = self.env.cr
        uid = self.env.user.id
        sale_order_line_obj = self.pool.get('sale.order.line')
        sale_order_lines = sale_order_line_obj.search(cr, uid, [('order_id', '=', self.id)])
        if sale_order_lines:
            category_dic = {}
            summary = ""
            for sale_order_line in sale_order_line_obj.browse(cr, uid,sale_order_lines):
                category_name = sale_order_line.product_id.categ_id.name
                if category_dic.has_key(category_name):
                    category_dic[category_name] += sale_order_line.product_uom_qty
                else:
                    category_dic[category_name] = sale_order_line.product_uom_qty
            for cat_name in category_dic.keys():
                summary += '%s: %s\n'%(cat_name, str(category_dic.get(cat_name, 0)))
            if self.products_summary != summary:
                self.products_summary = summary
        else:
            if self.products_summary != "":
                self.products_summary = ""

class sale_order_line_with_total(models.Model):
    _inherit = 'sale.order.line'

    line_total_price = fields.Float(compute='_compute_price_tax',string="Total TVAC", store=True)

    @api.one
    @api.depends('price_unit', 'product_uom_qty', 'free', 'product_id')
    def _compute_price_tax(self):

        if self.free:
            self.line_total_price = 0
        else:
            self.line_total_price = self.price_unit * self.product_uom_qty
