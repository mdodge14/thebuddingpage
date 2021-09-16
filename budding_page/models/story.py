# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models, tools, SUPERUSER_ID, _

_logger = logging.getLogger(__name__)


class Story(models.Model):
    _name = "story"
    _description = "Story"
    _order = "name"

    name = fields.Char(index=True)
    version_ids = fields.One2many('story.version', 'story_id', copy=True)
    current_version_id = fields.Many2one('story.version')
    chapter_ids = fields.One2many('chapter', 'story_id', copy=True)


class StoryVersion(models.Model):
    _name = "story.version"
    _description = "Story Version"
    _order = "version"

    story_id = fields.Many2one('story')
    version = fields.Integer(index=True)
    chapter_ids = fields.One2many('chapter', 'story_id', copy=True)
