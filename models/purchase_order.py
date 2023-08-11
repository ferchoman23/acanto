# -*- coding: utf-8 -*-

import time
from odoo.exceptions import UserError, ValidationError
from odoo import api, fields, models, _
import requests
import logging
import base64
from lxml import etree
from lxml.builder import ElementMaker
import xml.etree.ElementTree as ET
import datetime

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    fecha_receptionPago = fields.Date(
        string='Fecha de recepcion'
    )

    fecha_pago = fields.Date(
        string='Fecha de pago'
    )
    observacion_pago = fields.Char (
        string='Observaciones'
    )
    fecha_factura = fields.Date(
        String ='Fecha factura' 
    )
