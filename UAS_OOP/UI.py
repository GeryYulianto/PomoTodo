# UI.py

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
from services import TodoServices
from kink import inject

@inject
class UIPomodoroTodo():
    def __init__(self, _pomoservice:TodoServices):
        self.service = _pomoservice

    def init(self):
        # Make window
        window = tk.Tk()
        window.geometry("700x400")

        # Make Header
        header = tk.Label(text="Todo Apps & Pomodoro Timer", foreground="white", background="black")
        header.pack()

        self.create_pomodoro(window)

        self.create_todo()

        self.refresh_ui()

        window.mainloop()

    def create_pomodoro(self, window):
        # Create Header
        header_pomodoro = tk.Label(text="Pomodoro Timer", font=("buffalo", 20, "bold"), fg="gray")
        header_pomodoro.place(x=50, y=30)

        # Display Timer
        timer_label = tk.Label(text="Timer", font=("arial", 30, "bold"), fg="red")
        timer_label.place(x=100, y=100)

        def countdown(minutes, seconds):
            if minutes >= 0 and seconds >= 0:
                timer_label.config(text=f"{minutes:02d}:{seconds:02d}")

                if seconds == 0:
                    minutes -= 1
                    seconds = 59
                    if minutes < 5:
                        self.service.under_5_minutes()
                else:
                    seconds -= 1

                window.after(1000, countdown, minutes, seconds)
            if minutes == 0 and seconds == 0:
                button["state"] = "normal"
                button_short_break['state'] = 'normal'
                self.notfication_window('timesup')

        def min25():
            countdown(5, 2)

        def min5():
            countdown(5, 0)

        def disablebutton(button):
            button["state"] = "disabled"
            button_short_break["state"] = "disabled"

        # Button for pomodoro timer
        button = tk.Button(text="Start Pomodoro!", command=lambda: [min25(), disablebutton(button)], width=15, height=1,
                           bg="white", fg="black")
        button.place(x=50, y=300)

        button_short_break = tk.Button(text="Short Break!", command=lambda: [min5(), disablebutton(button)], width=10,
                                       height=1, bg="white", fg="black")
        button_short_break.place(x=180, y=300)

    def create_todo(self):
        # Create Header
        header_todo = tk.Label(text="Todo List :)", font=("buffalo", 20, "bold"), fg="gray")
        header_todo.place(x=370, y=30)

        def get_todo():
            text1 = entry_todo1.get()
            entry_todo1.delete(0, tk.END)

            text2 = entry_todo2.get()
            entry_todo2.delete(0, tk.END)

            result = self.service.insert_data(text1, text2)

            # Add these lines to update the list immediately

            if result:
                self.notfication_window("insert")
                self.refresh_ui() 
            else:
                showerror("Error", "Failed to insert data. Please try again.")

        # Entry
        entry_todo1 = tk.Entry(fg="white", bg="blue", width=30)
        entry_todo1.insert(0, "Enter Category")
        entry_todo1.place(x=400, y=300)

        entry_todo2 = tk.Entry(fg="white", bg="blue", width=30)
        entry_todo2.insert(0, "Enter Todo")
        entry_todo2.place(x=400, y=330)

        button_submit_todo = tk.Button(text="Submit", command=get_todo, width=10, height=1, bg="black", fg="white")
        button_submit_todo.place(x=400, y=350)

        # Label condition
        label_condition = tk.Label(text="")
        label_condition.place(x=370, y=370)

        # delete Button
        self.create_delete_button()

    def create_list(self, all_data):
        frame = tk.Frame(width=200, height=100, bg="red")
        frame.place(x=380, y=70)

        text_box = tk.Text(master=frame, width=30, height=13, wrap=tk.WORD)
        text_box.pack(fill=tk.BOTH)

        # Clear the existing content
        text_box.delete(1.0, tk.END)
        if all_data:
            for indx, dto in enumerate(all_data):
                text_box.insert(f"{indx + 1}.0", f"{indx + 1}. Category: {dto.category} Data: {dto.data}\n")
        else:
            self.service.notify_notodo()

    def create_delete_button(self):
        def delete_all_data():
            self.service.delete_all_todo()
            self.refresh_ui()
        
        # def delete_data():
        #     text1 = entry_todo1.get()
        #     entry_todo1.delete(0, tk.END)

        #     text2 = entry_todo2.get()
        #     entry_todo2.delete(0, tk.END)

        #     self.service.delete_specific_data([text1, text2])
        #     self.refresh_ui()

        delete_all_data_button = tk.Button(text="Delete All", command= delete_all_data,
                                           width=10, height=1, bg='red', fg='white')
        delete_all_data_button.place(x=480, y=350)

        # delete_button = tk.Button(text="Delete", command= delete_data,
        #                                    width=10, height=1, bg='red', fg='white')
        # delete_button.place(x=480, y=350)

    def refresh_ui(self):
        # Refresh UI components based on the current data
        all_data = self.service.get_data()
        self.create_list(all_data)
            
    def notfication_window(self, action):
        window = tk.Toplevel()
        window.geometry("200x100")
        if action == "insert":
            text = tk.Label(window, text=f"Inserted successfully!")
            text.pack()
        if action == "timesup":
            text = tk.Label(window, text=f"Times Up!")
            text.pack()

