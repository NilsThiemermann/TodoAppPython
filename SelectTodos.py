from tkinter import *
import sqlite3
from tkinter.font import BOLD

import app

conn = sqlite3.connect('todo.db')

widgets = []

class Select:

    def __init__(self, master):
        
        cur = conn.cursor()

        cur.execute("""SELECT * FROM view_Todo""")
        selected = cur.fetchall()

        total_rows = len(selected)
        total_columns = len(selected[0])

        titles = ["Todo:", "Zeitaufwand:", "Wichtigkeit:", "Erstell Datum:", "Wird Gemacht bis:"]
        
        for i in range(total_rows):
            for j in range(total_columns):
                self.la = Label(master, text=titles[j], width=18, fg='black', font=('Arial', 10, UNDERLINE))
                self.la.grid(row=1, column=j)
                self.l = Label(master, text=selected[i][j], width=18, fg='black', font=('Arial', 10))
                self.l.grid(row=i+2, column=j)
                widgets.append(self.la)
                widgets.append(self.l)

        self.btnCreate = Button(master, text="Create Todo", command=self.createTodos)
        self.btnCreate.grid(row=total_rows+3, column=total_columns)
        widgets.append(self.btnCreate)

    def createTodos():
        #remove the widgets from the frame
        app.forget(widgets)
        return app.createTodos()