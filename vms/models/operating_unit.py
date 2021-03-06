
# -*- coding: utf-8 -*-
# © <2012> <Israel Cruz Argil, Argil Consulting>
# © <2016> <Jarsa Sistemas, S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class OperatingUnit(models.Model):
    _inherit = 'operating.unit'
    _description = 'Base'

    order_sequence_id = fields.Many2one(
        'ir.sequence', string='Order Sequence')
    report_sequence_id = fields.Many2one(
        'ir.sequence', string='Report Sequence')
