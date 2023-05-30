from odoo import models, fields


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    autorizado_por = fields.Char(string='Autorizado por')
    recibido_por = fields.Char(string='Recibido por')
    tipo_pago = fields.Selection([('cheque', 'Cheque'), ('transferencia', 'Transferencia')],
                                 string='Tipo de pago')
