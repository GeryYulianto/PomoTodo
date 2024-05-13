from services import *
from observer import *
from database import TodoDB
from subject import SubjectTodo, Message
from dto import *
from abc import ABC, abstractmethod
from kink import di, inject


class MockIObserver(ABC):
    @abstractmethod
    def notified(self, message):
        pass


@inject(alias=MockIObserver)
class MockObserverCongratsNoTodo(MockIObserver):
    def notified(self, message):
        if message.action == 'notodo':
            return "notodo"

@inject(alias=MockIObserver)
class MockObserverExceeding3Todo(MockIObserver):
    def notified(self, message):
        if message.action == "insert":
            if message.data > 3:
                return "exceeding"

@inject(alias=MockIObserver)
class MockObserverMinutesLessThanFive(IObserver):
    def notified(self, message):
        if message.action == "<5":
            return "5 minutes"

@inject
class MockSubject(SubjectTodo):
    def __init__(self, observers:list[MockIObserver]):
        self.observers = observers
    
    def notify_observers(self, message):
        result_all = []
        for observer in self.observers:
            result = observer.notified(message)
            result_all.append(result)
        return result_all




di['dbunit'] = True
di[TodoServices] = TodoServices(di[todoDBsql], di[MockSubject])
service = di[TodoServices]
db = di[todoDBsql]
subject = di[MockSubject]

def test_notify_exceeding():
    db.delete_data('all')
    service.insert_data("belajar", "sejarah")
    service.insert_data("kerja", "OOP")
    service.insert_data("makan", "ayam")
    result = service.insert_data("minum", "air")
    expected = [None, "exceeding", None]
    assert result == expected