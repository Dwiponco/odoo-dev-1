from odoo import models, fields

class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Estate Property Tag'
    _order = 'name asc'

    name = fields.Char(string='Name', required=True)
    property_ids = fields.Many2many(string='Properties', comodel_name='estate.property', inverse_name='tag_ids')
    color = fields.Integer(string='Color')

    _sql_constraints = [
        ('check_name', 'UNIQUE(name)', 'Name must be unique'),
    ]