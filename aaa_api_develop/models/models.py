# -*- coding: utf-8 -*-

from odoo import models, fields, api


class aaa_api_develop(models.Model):
    _name = 'model'
    _description = 'aaa_api_develop.aaa_api_develop'

    name = fields.Char()
    phone = fields.Char()
    email_from = fields.Char()
    team_id = fields.Char()


