# subject.py
from abc import ABC, abstractmethod
from observer import IObserver
from kink import inject

@inject
class SubjectTodo:
    def __init__(self, observers:list[IObserver]):
        self.observers = observers

    def attach(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.notified(message)

class Message:
    def __init__(self, _action, _data=None):
        self.action = _action
        self.data = _data