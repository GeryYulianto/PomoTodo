# database.py
import sqlite3
from abc import ABC
from dto import DTO
from kink import inject

class TodoDB(ABC):
    def init(self):
        pass

    def insert_data(self, data):
        pass

    def get_all_data(self):
        pass

    def delete_data(self, data):
        pass

@inject(alias=TodoDB)
class todoDBsql(TodoDB):
    def __init__(self, dbunit:bool):
        self.todo_db = sqlite3.connect('todo.db')
        self.cur = self.todo_db.cursor()
        if dbunit == "true":
            self.create_table()
            self.delete_all_todo()

    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Todo
        (category TEXT, todo TEXT)''')
        self.todo_db.commit()

    def insert_todo_data(self, category, todo):
        self.cur.execute("INSERT INTO Todo VALUES (?, ?)", (category, todo))
        self.todo_db.commit()
        return True

    def get_all_data(self):
        self.cur.execute("SELECT category, todo FROM Todo")
        all_data = self.cur.fetchall()
        all_dto = []
        for data in all_data:
            all_dto.append(DTO(data[0], data[1]))
        return all_dto

    def delete_data(self, data):
        if data.lower() == 'all':
            self.cur.execute("DELETE FROM Todo")
            self.todo_db.commit()
            return self.get_all_data()
        else:
            self.cur.execute("""DELETE FROM Todo
            WHERE category = ? and todo = ?""", (data[0], data[1]))
            self.todo_db.commit()
            return self.get_all_data()

    def get_recent_inserted_data(self):
        self.cur.execute("SELECT category, todo FROM Todo LIMIT 1")
        recent_data = self.cur.fetchone()

        if recent_data:
            return DTO(recent_data[0], recent_data[1])
        else:
            return None

    def get_row_count(self):
        self.cur.execute("SELECT COUNT(*) FROM Todo")
        row_count = self.cur.fetchone()[0]
        return row_count
