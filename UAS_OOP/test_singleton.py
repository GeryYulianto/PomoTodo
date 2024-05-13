from services import TodoServices
from observer import IObserver
from database import TodoDB
from UI import UIPomodoroTodo
from dto import *
from abc import ABC, abstractmethod
from kink import di, inject

di['dbunit'] = True

def test_singletone_service():
    service_id = id(di[TodoServices])
    service_id_from_ui = id(di[UIPomodoroTodo].service)
    assert service_id == service_id_from_ui

def test_singletone_db():
    db_id = id(di[TodoDB])
    db_id_from_service = id(di[TodoServices].db)
    assert db_id == db_id_from_service

test_singletone_db()