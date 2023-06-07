from odoo import fields, models

class ResCompany(models.Model):
    _inherit = 'res.company'
    
    dia_pago = fields.Char (
        string='Día de pago'
    )
    
    horario_pago = fields.Char (
        string='Horario de pago'
    )


    