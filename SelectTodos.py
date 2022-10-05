from tkinter import *
import sqlite3
from tkinter.font import BOLD
from tkinter.tix import AUTO

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

        titles = ["Id:", "Todo:", "Zeitaufwand:", "Wichtigkeit:", "Erstell Datum:", "Wird Gemacht bis:","Delete"]

        for i in range(len(titles)):
            self.la = Label(master, text=titles[i], width=18, fg='black', font=('Arial', 10, UNDERLINE))
            self.la.grid(row=1, column=i)
            widgets.append(self.la)

        for i in range(total_rows):
            for j in range(total_columns):
                self.l = Label(master, text=selected[i][j], width=18, fg='black', font=('Arial', 10))
                self.l.grid(row=i+2, column=j)
                
                
                widgets.append(self.l)

            self.d = Button(master, text="Delete", command= lambda: self.deleteTodo(selected[i][0]))
            self.d.grid(row=i+2, column=total_columns)
            widgets.append(self.d)

        self.btnCreate = Button(master, text="Create Todo", command=self.createTodos)
        self.btnCreate.grid(row=total_rows+3, column=total_columns)
        widgets.append(self.btnCreate)        

    def createTodos(_):
        #remove the widgets from the frame
        app.grid_forget(widgets)
        return app.createTodos()

    def deleteTodo(_, id):
        app.grid_forget(widgets)
        return app.deleteTodo(id)