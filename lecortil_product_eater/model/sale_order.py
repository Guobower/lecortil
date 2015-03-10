from openerp import models, fields, api

class sale_order_eater(models.Model):
    _inherit = 'sale.order'

    eater = fields.Many2one('cortil.eater', string="Consommateur")
    
    def action_button_confirm_custom(self, cr, uid, ids, context=None):
        sale_order = self.pool.get('sale.order').browse(cr, uid, ids, context)
        if sale_order:
            for sale_order_line in sale_order.order_line:
                if sale_order_line.eater and sale_order_line.eater.id and sale_order.partner_id.id != sale_order_line.eater.partner.id:
                    self.pool.get('cortil.eater').write(cr, uid, sale_order_line.eater.id, {'partner': sale_order_line.order_id.partner_id.id})      
        return super(sale_order_eater, self).action_button_confirm(cr, uid, ids, context)
