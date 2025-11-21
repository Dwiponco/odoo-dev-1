from odoo import models, fields

class EstatePropertyType(models.Model):
    _name="estate.property.type"
    _description="Estate Property Type"

    name=fields.Char(string="Name", required=True, unique=True)

    _sql_constraints = [
        ('check_name', 'UNIQUE(name)', 'Name must be unique'),
    ]