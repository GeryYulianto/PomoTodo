# services.py
from subject import SubjectTodo, Message
from observer import ObserverExceeding3Todo, ObserverCongratsNoTodo, ObserverMinutesLessThanFive
from database import todoDBsql
from kink import inject,di

@inject
class TodoServices():
    def __init__(self, _todo_db:todoDBsql, _subject:SubjectTodo):
        self.subject = _subject
        self.db = _todo_db
        self.startup()

    def insert_data(self, category, todo):
        self.db.insert_todo_data(category, todo)
        return self.subject.notify_observers(Message("insert", self.db.get_row_count()))

    def under_5_minutes(self):
        message = Message("<5")
        self.subject.notify_observers(message)
    
    def notify_notodo(self):
        message = Message("notodo")
        self.subject.notify_observers(message)

    def startup(self):
        data = self.db.get_all_data()
        return data

    def delete_all_todo(self):
        self.db.delete_data('all')

    def get_data(self):
        return self.db.get_all_data()
    
    def delete_specific_data(self, data):
        category = data[0]
        todo = data[1]
        self.db.delete_data([category, todo])
