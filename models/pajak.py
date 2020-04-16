# -*- coding: utf-8 -*-

from odoo import models, fields, api,_

class vit_bills_pajak(models.Model):
		_inherit='account.invoice'

		pajak_ids = fields.One2many(comodel_name="pajak.masukan",
									inverse_name="pajak_id",
									string="Pajak Masukan",
									required=False)



class pajak_masukan(models.Model):
		_name = 'pajak.masukan'
		_rec_name = 'nomor'


		nomor = fields.Char(string='Nomor')
		amount = fields.Integer(string="Amount")

		pajak_id = fields.Many2one(comodel_name='account.invoice', string='Account Pajak')
