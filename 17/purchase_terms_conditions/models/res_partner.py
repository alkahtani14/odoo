from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    purchase_note = fields.Html(
        string="Purchase Default Terms and Conditions", translate=True
    )
