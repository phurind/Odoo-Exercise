# from odoo import models, fields

# class TodoItem(models.Model):
#     _name = 'todo.item'
#     _description = 'Todo Item'

#     name = fields.Char(string='Item Name', required=True)
#     description = fields.Text(string='Description')
#     is_done = fields.Boolean(string='Done')
#     todo_id = fields.Many2one('todo.list', string='Todo List')

from odoo import models, fields

class TodoItem(models.Model):
    _name = 'todo.item'
    _description = 'Todo Item'

    name = fields.Char(string='Item Name', required=True)
    description = fields.Text(string='Description')
    is_done = fields.Boolean(string='Is Done', default=False)
    todo_id = fields.Many2one('todo.list', string='Todo List', ondelete='cascade')