from services import TodoServices
from observer import IObserver
from database import todoDBsql
from UI import UIPomodoroTodo
from dto import *
from abc import ABC, abstractmethod
from kink import di, inject
import sqlite3

@inject
class MockDB(todoDBsql):
    def init(self, dbunit: bool):
        super().init(dbunit)
        self.todo_db = sqlite3.connect('./mockdb.db')
        self.create_table()

    def create_sample(self):
        self.insert_todo_data('cate','data')

di['dbunit'] = True
service = di[TodoServices]
db = di[MockDB]

def test_del_alldata():
    db.delete_data('all')
    all_dto = db.get_all_data()
    result = db.get_row_count()
    expected = 0

    assert result == expected

test_del_alldata()

def test_get_alldata():
    db.delete_data('all')
    db.create_sample()
    all_dto = db.get_all_data()
    expected = ['cate', 'data']
    result = [all_dto[0].category, all_dto[0].data]

    assert result == expected

