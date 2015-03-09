from openerp import models, fields, api
    
class sale_order_linked_products(models.Model):
    _inherit = 'sale.order'
    
    def add_linked_products(self, cr, uid, ids, context=None):
        sale_order_obj = self.pool.get('sale.order')
        sale_order = sale_order_obj.browse(cr, uid,ids[0])
        sale_order_line_obj = self.pool.get('sale.order.line')
        sale_order_lines = sale_order_line_obj.search(cr, uid, [('order_id', '=', sale_order.id)])
        if sale_order_lines:
            product_product_linked_obj = self.pool.get('product.product.linked')
            for sale_order_line in sale_order_line_obj.browse(cr, uid,sale_order_lines):
                if sale_order_line.is_linked_products == False:
                    cr.execute('select product_product_linked_id from product_product_linked_product_template_rel where product_template_id=%s', (str(sale_order_line.product_id.product_tmpl_id.id),))
                    for linked_product_id in cr.fetchall():
                        
                        #with open('/var/log/odoo/odoo-server.log', 'a') as f:
                        #    f.write("\nDEBUG: query result (product_product_linked_id) : "+str(linked_product_id[0])+"\n")
                        
                        linked_product = product_product_linked_obj.browse(cr, uid, linked_product_id[0])
                        
                        if linked_product.child_product.property_account_income.id:
                            invoice_line_account_id = linked_product.child_product.property_account_income.id
                        else:
                            invoice_line_account_id = linked_product.child_product.categ_id.property_account_income_categ.id

                        sale_order_line_id = sale_order_line_obj.create(cr,uid,{
                            'delay': 1,#Required, Delivery Lead Time
                            #'name' : linked_product.child_product.description_sale, #Required, Description
                            'order_id': sale_order.id, #Required, Order Reference
                            'price_unit': linked_product.child_product.lst_price, #Required, Unit Price
                            'product_uom': linked_product.child_product.uom_id.id, #Required, Unit of Measure
                            'product_uom_qty': linked_product.quantity, #Required, Quantity
                            'state': 'draft', #Required, State (selection)
                            'product_id': linked_product.child_product.id, #Product
                            'company_id': sale_order.company_id.id, #Company
                            })
                    sale_order_line.is_linked_products = True
            return {
                    'type': 'ir.actions.client',
                    'tag': 'reload',
                    }