# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models, tools, SUPERUSER_ID, _

_logger = logging.getLogger(__name__)


class Passage(models.Model):
    _name = "passage"
    _description = "Chapter"
    _order = "sequence"

    sequence = fields.Integer(required=True, default=10)
    version = fields.Integer(index=True)
    text = fields.Text()
    chapter_id = fields.Many2one('chapter')
    version_ids = fields.One2many('passage.version', 'passage_id', copy=True)
    current_version_id = fields.Many2one('passage.version')


class PassageVersion(models.Model):
    _name = "passage.version"
    _description = "Passage Version"
    _order = "version"

    passage_id = fields.Many2one('passage')
    version = fields.Integer(index=True)
    text = fields.Text()
