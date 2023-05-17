# -*- coding: utf-8 -*-
from odoo import api, models
import re
import datetime
from datetime import date
import logging

class ReportContraseiaPago(models.AbstractModel):
    _name = 'report.acanto.contrasenia_pago_report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['account.move'].browse(docids)


        return {
            'doc_ids': docids,
            'doc_model': 'account.move',
            'docs': docs,
        }