from odoo import fields, models
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