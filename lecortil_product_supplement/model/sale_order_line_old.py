from openerp.osv import fields,osv
import openerp.addons.decimal_precision as dp

class sale_order_line_amount_line_product_supplements(osv.osv):
       
    def product_id_change(self, cr, uid, ids, pricelist, product, qty=0, uom=False, qty_uos=0, uos=False, name='', partner_id=False,lang=False, update_tax=True, date_order=False, packaging=False, fiscal_position=False, flag=False, context=None):
        res = super(sale_order_line_amount_line_product_supplements, self).product_id_change(cr, uid, ids, pricelist, product, qty, uom, qty_uos, uos, name, partner_id, lang, update_tax, date_order, packaging, fiscal_position, flag, context)
        if res.has_key('value') and res['value'].has_key('price_unit'):
            res['value']['product_price_unit']=res['value']['price_unit']
        return res
    
    def _amount_line_product_supplements(self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        tax_obj = self.pool.get('account.tax')
        cur_obj = self.pool.get('res.currency')
        if context is None:
            context = {}
        for line in self.browse(cr, uid, ids, context=context):
            #Existing method
            #price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)

            #Lines added to the existent method
            if line.free == True:
                price = 0
                line_price_unit = int(line.price_unit*1000)/1000.0
                if line_price_unit != 0:
                    line.price_unit = 0
            else:
                price = line.product_price_unit
                if line.supplement_products_ids:
                    for supplement_product in line.supplement_products_ids:
                        price += supplement_product.lst_price
                
                    if price <= line.product_price_unit:
                        price = line.product_price_unit
                    
                price_test = int(price*1000)/1000.0
                price_unit_test = int(line.price_unit*1000)/1000.0
                if price_test > 0 and price_unit_test != price_test:
                    line.price_unit = price

            taxes = tax_obj.compute_all(cr, uid, line.tax_id, price, line.product_uom_qty, line.product_id, line.order_id.partner_id)
            cur = line.order_id.pricelist_id.currency_id
            res[line.id] = cur_obj.round(cr, uid, cur, taxes['total'])
        return res
 
    _inherit = 'sale.order.line'
    
    _columns = { 
        'price_subtotal': fields.function(_amount_line_product_supplements, string='HTVA', digits_compute= dp.get_precision('Account')),
    }
