from odoo import models, fields

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