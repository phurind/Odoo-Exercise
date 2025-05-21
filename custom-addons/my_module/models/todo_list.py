from odoo import models, fields, api
from odoo.exceptions import ValidationError  

class TodoList(models.Model):
    _name = 'todo.list'
    _description = 'Todo List'

    name = fields.Char(string='Name', required=True)
    tag_ids = fields.Many2many('todo.tag', string='Tags')
    date_start = fields.Date(string='Start Date', required=True)
    date_end = fields.Date(string='End Date', required=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('complete', 'Complete')
    ], default='draft', string='Status')
    item_ids = fields.One2many('todo.item', 'todo_id', string='Items')
    participant_ids = fields.Many2many('res.users', string='Participants')

    @api.constrains('date_start', 'date_end')
    def _check_dates(self):
        for rec in self:
            if rec.date_end < rec.date_start:
                raise ValidationError('End date must be after start date')

    def action_start(self):
        for rec in self:
            if rec.status != 'draft':
                raise ValidationError("Only Draft tasks can be started.")
            rec.status = 'in_progress'

    def action_complete(self):
        for rec in self:
            if rec.status != 'in_progress':
                raise ValidationError("Only In Progress tasks can be completed.")
            rec.status = 'complete'
