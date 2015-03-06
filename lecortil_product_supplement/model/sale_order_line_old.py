from openerp.osv import fields,osv
import openerp.addons.decimal_precision as dp

class sale_order_line_amount_line_product_supplements(osv.osv):
       
    def _amount_line_product_supplements(self, cr, uid, ids, field_name, arg, context=None):
        #res = super(sale_order_line_amount_line_product_supplements, self)._amount_line(cr, uid, ids, field_name, arg, context)
        res = {}
        tax_obj = self.pool.get('account.tax')
        cur_obj = self.pool.get('res.currency')
        if context is None:
            context = {}
        for line in self.browse(cr, uid, ids, context=context):
            #lines added to the existent method
            lst_price = line.product_id.lst_price
            price = lst_price
            if line.supplement_products_ids:
                for supplement_product in line.supplement_products_ids:
                    price += supplement_product.lst_price
            if price < lst_price:
                price = lst_price
            if line.price_unit != price:
                line.price_unit = price

            #price = price * (1 - (line.discount or 0.0) / 100.0)
            taxes = tax_obj.compute_all(cr, uid, line.tax_id, price, line.product_uom_qty, line.product_id, line.order_id.partner_id)
            cur = line.order_id.pricelist_id.currency_id
            res[line.id] = cur_obj.round(cr, uid, cur, taxes['total'])
        return res
 
    _inherit = 'sale.order.line'
    
    _columns = { 
        'price_subtotal': fields.function(_amount_line_product_supplements, string='HTVA', digits_compute= dp.get_precision('Account')),
    }
