from odoo import api, models, fields
from datetime import timedelta

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate Property Offer'

    price = fields.Float(string='Price', required=True)
    status = fields.Selection(
        [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('refused', 'Refused')
        ],
        string='Status', default='pending', copy=False)
    partner_id = fields.Many2one(string='Partner', comodel_name='res.partner', required=True, copy=False)
    property_id = fields.Many2one(string='Property', comodel_name='estate.property', required=True, copy=False)
    validity = fields.Integer(string='Validity (days)', default=7)
    date_deadline = fields.Date(string='Deadline', compute='_compute_date_deadline', inverse='_inverse_date_deadline')

    @api.depends('create_date', 'validity')
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date + timedelta(days=record.validity)
            else:
                record.date_deadline = fields.Date.today() + timedelta(days=record.validity)


    def _inverse_date_deadline(self):
        for record in self:
            if record.date_deadline and record.create_date:
                delta = record.date_deadline - record.create_date
                record.validity = delta.days
            else:
                record.validity = (record.date_deadline - fields.Date.today()).days