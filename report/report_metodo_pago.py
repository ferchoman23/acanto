# -*- coding: utf-8 -*-
from odoo import api, models
import re
import datetime
from datetime import date
import logging

class ReportMetodoPago(models.AbstractModel):
    _name = 'report.acanto.metodo_pago_report'

    def num_a_letras(self, num, completo=True):
        en_letras = {
            '0': 'cero',
            '1': 'uno',
            '2': 'dos',
            '3': 'tres',
            '4': 'cuatro',
            '5': 'cinco',
            '6': 'seis',
            '7': 'siete',
            '8': 'ocho',
            '9': 'nueve',
            '10': 'diez',
            '11': 'once',
            '12': 'doce',
            '13': 'trece',
            '14': 'catorce',
            '15': 'quince',
            '16': 'dieciseis',
            '17': 'diecisiete',
            '18': 'dieciocho',
            '19': 'diecinueve',
            '20': 'veinte',
            '21': 'veintiuno',
            '22': 'veintidos',
            '23': 'veintitres',
            '24': 'veinticuatro',
            '25': 'veinticinco',
            '26': 'veintiseis',
            '27': 'veintisiete',
            '28': 'veintiocho',
            '29': 'veintinueve',
            '3x': 'treinta',
            '4x': 'cuarenta',
            '5x': 'cincuenta',
            '6x': 'sesenta',
            '7x': 'setenta',
            '8x': 'ochenta',
            '9x': 'noventa',
            '100': 'cien',
            '1xx': 'ciento',
            '2xx': 'doscientos',
            '3xx': 'trescientos',
            '4xx': 'cuatrocientos',
            '5xx': 'quinientos',
            '6xx': 'seiscientos',
            '7xx': 'setecientos',
            '8xx': 'ochocientos',
            '9xx': 'novecientos',
            '1xxx': 'un mil',
            'xxxxxx': 'mil',
            '1xxxxxx': 'un millón',
            'x:x': 'millones'
        }

        num_limpio = str(num).replace(',','')
        partes = num_limpio.split('.')

        entero = 0
        decimal = 0
        if partes[0]:
            entero = str(int(partes[0]))
        if len(partes) > 1 and partes[1]:
            # Los decimales no pueden tener mas de dos digitos
            decimal = partes[1][0:2].ljust(2,'0')

        num_en_letras = 'ERROR'
        if int(entero) < 30:
            num_en_letras = en_letras[entero]
        elif int(entero) < 100:
            num_en_letras = en_letras[entero[0] + 'x']
            if entero[1] != '0':
                num_en_letras = num_en_letras + ' y ' + en_letras[entero[1]]
        elif int(entero) < 101:
            num_en_letras = en_letras[entero]
        elif int(entero) < 1000:
            num_en_letras = en_letras[entero[0] + 'xx']
            if entero[1:3] != '00':
                num_en_letras = num_en_letras + ' ' + self.num_a_letras(entero[1:3], False)
        elif int(entero) < 2000:
            num_en_letras = en_letras[entero[0] + 'xxx']
            if entero[1:4] != '000':
                num_en_letras = num_en_letras + ' ' + self.num_a_letras(entero[1:4], False)
        elif int(entero) < 1000000:
            miles = int(entero.rjust(6)[0:3])
            cientos = entero.rjust(6)[3:7]
            num_en_letras = self.num_a_letras(str(miles), False) + ' ' + en_letras['xxxxxx']
            if cientos != '000':
                num_en_letras = num_en_letras + ' ' + self.num_a_letras(cientos, False)
        elif int(entero) < 2000000:
            num_en_letras = en_letras[entero[0] + 'xxxxxx']
            if entero[1:7] != '000000':
                num_en_letras = num_en_letras + ' ' + self.num_a_letras(entero[1:7], False)
        elif int(entero) < 1000000000000:
            millones = int(entero.rjust(12)[0:6])
            miles = entero.rjust(12)[6:12]
            num_en_letras = num_a_letras(str(millones), False) + ' ' + en_letras['x:x']
            if miles != '000000':
                num_en_letras = num_en_letras + ' ' + self.num_a_letras(miles, False)

        if not completo:
            return num_en_letras

        if decimal == 0:
            letras = '%s exactos' % num_en_letras
        else:
            letras = '%s con %s/100' % (num_en_letras, decimal)

        return letras


    def a_letras(self,monto):
        logging.warning('Ingreso???')
        logging.warning(monto)
        logging.warning(self.num_a_letras(monto))
        return self.num_a_letras(monto,False)

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['account.payment'].browse(docids)

        

        return {
            'doc_ids': docids,
            'doc_model': 'account.payment',
            'docs': docs,
            'a_letras': self.a_letras,

        }