# -*- coding: utf-8 -*-
# © <2016> <Jarsa Sistemas, S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from openerp import fields, models


class VmsVehicleCycle(models.Model):
    _description = 'Vms Vehicle Cycle'
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    _name = 'vms.vehicle.cycle'

    cycle_id = fields.Many2one(
        'vms.cycle',
        string='Cycle')
    schedule = fields.Float(
        required=True,
        default=True, string='Distance Schedule')
    sequence = fields.Integer(string='Sequence')
    order_id = fields.Many2one(
        'vms.order',
        string='Order')
    date = fields.Datetime()
    distance = fields.Float(default=0.0, string='Distance Real')
    unit_id = fields.Many2one(
        'fleet.vehicle',
        string="Unit",
        required=True)
