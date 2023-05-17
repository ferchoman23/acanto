from odoo import fields , models


class CRMLead(models.Model):
    _inherit = 'crm.lead'
    
    plazo_pago = fields.Many2one(
        string='plazo de pago',
        related='partner_id.property_payment_term_id', readonly=True,
    )
