from odoo import fields, models, api


class CRMLead(models.Model):
    _inherit = 'crm.lead'

    plazo_pago = fields.Many2one(
        string='plazo de pago',
        related='partner_id.property_payment_term_id', readonly=True,
    )
    fecha_inicio = fields.Date(string='Fecha Inicio')
    fecha_final = fields.Date(string='Fecha Final')
    productos_vendidos_ids = fields.Many2many('account.move.line')

    @api.onchange('fecha_inicio', 'fecha_final')
    def onchange_fecha(self):
        if self.fecha_inicio and self.fecha_final:
            move_lines = self.env['account.move.line'].search([
                ('move_id.invoice_date', '>=', self.fecha_inicio),
                ('move_id.invoice_date', '<=', self.fecha_final),
                ('move_id.partner_id', '=', self.partner_id.id),
                ('account_id.user_type_id.name', '=', 'Ingreso'),
                ('price_subtotal', '>', 0),
            ],order="date ASC")
            self.productos_vendidos_ids = [(6, 0, move_lines.ids)]
