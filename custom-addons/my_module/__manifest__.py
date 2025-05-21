{
    'name': 'Todo List',
    'version': '1.0',
    'summary': 'Module for managing todo lists',
    'category': 'Productivity',
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
       'security/ir.model.access.csv',
        'views/todo_action.xml',         
        'views/todo_menu.xml',
        'views/todo_list_view.xml',
        'views/todo_item_view.xml',
        'views/todo_tag_view.xml',
        'data/tag_data.xml',
    ],
    'installable': True,
    'application': True,
}