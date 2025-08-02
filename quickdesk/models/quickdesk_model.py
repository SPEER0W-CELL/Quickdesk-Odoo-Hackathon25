from odoo import models, fields

class QuickDeskTask(models.Model):
    _name = 'quickdesk.task'
    _description = 'QuickDesk Task'

    name = fields.Char(string='Task Name', required=True)
    description = fields.Text(string='Description')
    progress = fields.Integer(string='Progress (%)')
    is_quest = fields.Boolean(string='Is RPG Quest?', default=False)