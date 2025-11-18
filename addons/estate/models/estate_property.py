import copy
from odoo import _, api, fields, models
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'

    name = fields.Char(string='Name', required=True, default='Unknown')
    description = fields.Text()
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(string='Date Availability', copy=False, default=lambda self: fields.Datetime.now() + relativedelta(months=3))
    expected_price = fields.Float(string='Expected Price', required=True)
    selling_price = fields.Float(string='Selling Price', readonly=True, copy=False)
    bedrooms = fields.Integer(string='Bedrooms')
    living_area = fields.Integer(string='Living Area (sqm)')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden Area (sqm)')
    garden_orientation = fields.Selection(
        [
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
        ], 
        string='Garden Orientation'
        )
    active = fields.Boolean(string='Active', default=False)
    state = fields.Selection(
        [
        ('new', 'New'), 
        ('offer_received', 'Offer Received'), 
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled')
        ], 
        string='State', 
        default='new',
        required=True,
        copy=False,
        )
    property_type_id = fields.Many2one(string='Property Type', comodel_name='estate.property.type')
    salesperson_id = fields.Many2one('res.users', string='Salesman', index=True, default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.partner', string='Buyer', index=True, copy=False)
    tag_ids = fields.Many2many(string='Tags', comodel_name='estate.property.tag')
    offer_ids = fields.One2many(string='Offers', comodel_name='estate.property.offer', inverse_name='property_id')
    total_area = fields.Float(string='Total Area (sqm)', compute='_compute_total_area')
    best_price = fields.Float(string='Best Offer', compute='_compute_best_price')

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = sum([(record.living_area or 0), (record.garden_area or 0)])

    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            if record.offer_ids:
                record.best_price = max(record.offer_ids.mapped('price'))
            else:
                record.best_price = 0
    
    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'north'
            return {
                'warning': {
                    'title': _('Garden'),
                    'message': _('The garden has been enabled and the garden area and orientation have been set to 10 and north respectively.')
                }
            }
        else:
            self.garden_area = None
            self.garden_orientation = None