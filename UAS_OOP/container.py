#container
from UI import UIPomodoroTodo
from database import todoDBsql
from services import TodoServices
from kink import inject,di

@inject
class Container:
    def __init__(self, _db:todoDBsql, _service:TodoServices, _ui:UIPomodoroTodo ):
        self.db = _db
        self.services = _service
        self.ui = _ui 