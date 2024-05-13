#main
from UI import UIPomodoroTodo
from database import todoDBsql
from services import TodoServices
import argparse
from kink import di

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-dbunit", default="false")
    args = parser.parse_args()
    di["dbunit"] = True if args.dbunit.lower() == 'true' else False

if __name__ == "__main__":
    parse_args()
    ui = di[UIPomodoroTodo]
    service = di[TodoServices]
    ui.init()