from odoo import api, models, fields

class EstatePropertyType(models.Model):
    _name="estate.property.type"
    _description="Estate Property Type"
    _order = 'sequence, name'

    name=fields.Char(string="Name", required=True, unique=True)
    property_ids=fields.One2many(string="Properties", comodel_name="estate.property", inverse_name="property_type_id")
    sequence=fields.Integer(string="Sequence")
    offer_ids=fields.One2many('estate.property.offer', 'property_type_id', string="Offers")
    offer_count=fields.Integer(string="Offer Count", compute="_compute_offer_count")

    _sql_constraints = [
        ('check_name', 'UNIQUE(name)', 'Name must be unique'),
    ]

    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)  
