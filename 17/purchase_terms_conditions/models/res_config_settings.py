from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    purchase_note = fields.Html(
        related="company_id.purchase_note",
        string="Purchase Terms & Conditions",
        readonly=False,
    )

    use_purchase_note = fields.Boolean(
        string="Use Purchase Default Terms & Conditions",
        config_parameter="purchase.use_purchase_note",
    )
