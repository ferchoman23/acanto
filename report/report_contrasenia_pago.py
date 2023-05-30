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
        docs = self.env['purchase.order'].browse(docids)
        for doc in docs:
            origin_parts = doc.origin.split('-')
            part1 = origin_parts[0] if len(origin_parts) > 0 else ''
            part2 = origin_parts[1] if len(origin_parts) > 1 else ''

        return {
            'doc_ids': docids,
            'doc_model': 'purchase.order',
            'docs': docs,
            'part1': part1,
            'part2': part2,
        }
