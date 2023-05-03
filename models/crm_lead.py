from odoo import fields , models  


class CRMLead(models.Model):
    _inherit = 'crm.lead'


    #plazo_pago = fields.Char(String = "plazo de pago",related='parther_id.property_payment_term_id.name')
    #plazo_pago = fields.related('parther_id','property_payment_term_id',type='many2one', string ='plazos de pago', relation ='account.payment.term')

    plazo_pago = fields.Many2one(
        string='plazo de pago',
        related='partner_id.property_payment_term_id', readonly=True,
    )