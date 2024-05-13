# observer.py
from abc import ABC
from kink import inject

class IObserver(ABC):
    def notified(self, message):
        pass

@inject(alias=IObserver)
class ObserverExceeding3Todo(IObserver):
    def notified(self, message):
        if message.action == "insert":
            #Cek how many todo, if exceed then pop notif
            if message.data > 3:
                print(f"Your todo exceeding 3 ({message.data} task), please finish your task immediately!")

@inject(alias=IObserver)
class ObserverMinutesLessThanFive(IObserver):
    def notified(self, message):
        if message.action == "<5":
            print("5 More minutes! You can do it")

@inject(alias=IObserver)
class ObserverCongratsNoTodo(IObserver):
    def notified(self, message):
        if message.action == "notodo":
            print("Congrats you done all your task")
# class ObserverRefresh(IObserver):
#     def notified(self, message):
#         if message == "insert" or message == "delete":
            
