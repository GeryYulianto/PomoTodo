from services import TodoServices
from observer import IObserver
from database import TodoDB
from dto import *
from abc import ABC, abstractmethod
from kink import di, inject
import sqlite3

@inject
class MockDB(TodoDB):
    def __init__(self, dbunit:bool):
        self.todo_db = sqlite3.connect('mock_db.db')
        self.cur = self.todo_db.cursor()
        if dbunit == "true":
            self.create_table()
            self.delete_all_todo()

di['dbunit'] = False
service = di[TodoServices]
db = di[MockDB]



def test_insert_data():
    db.delete_data('all')
    service.insert_data('belajar', 'sejarah')
    product_dto = service.get_data()
    expected = [1,"belajar", 'sejarah']
    result = [len(product_dto), product_dto[0].category, product_dto[0].data]
    # (product_dto) == 1 and product_dto[0].name_item == 'll'
    print(product_dto)
    assert expected == result

test_insert_data()
