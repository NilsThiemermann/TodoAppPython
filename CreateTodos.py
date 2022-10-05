from tkinter import *
import sqlite3

import app

conn = sqlite3.connect('todo.db')

widgets= []

class Create:
    
    def __init__(self, master):

        titles = ["Todo:", "Zeitaufwand:", "Wichtigkeit:",  "Wird Gemacht bis:"]

        for i in range(len(titles)):
            self.l = Label(master, text=titles[i], fg='black', font=('Arial', 14))
            self.l.grid(row=i, column=1)
            widgets.append(self.l)

        self.e1 = Entry(master, fg='black', width=40, font=('Arial', 14))
        self.e1.grid(row=0, column=2)
        self.e2 = Entry(master, fg='black', width=40, font=('Arial', 14))
        self.e2.grid(row=1, column=2)
        self.e3 = Entry(master, fg='black', width=40, font=('Arial', 14))
        self.e3.grid(row=2, column=2)
        self.e4 = Entry(master, fg='black', width=40, font=('Arial', 14))
        self.e4.grid(row=3, column=2)

        widgets.append(self.e1)
        widgets.append(self.e2)
        widgets.append(self.e3)
        widgets.append(self.e4)

        self.btnSend = Button(master, text='Send', command=self.insertDB)
        self.btnSend.grid(row=5, column=2)
        self.btnSelect = Button(master, text="Show Todos", command=self.selectTodos)
        self.btnSelect.grid(row=5, column=3)

        widgets.append(self.btnSelect)  
        widgets.append(self.btnSend) 
        
    def insertDB(self):
        cur = conn.cursor()

        v1 = self.e1.get()
        v2 = self.e2.get()
        v3 = self.e3.get()
        v4 = self.e4.get()

        values = [v1, v2, v3, v4]

        sql = """INSERT INTO tbl_Todo(todo, expenditure_of_time, fk_importance, expiry_date) VALUES(?,?,?,?)"""

        cur.execute(sql, values)
        conn.commit()

        self.selectTodos()
    
    def selectTodos(_):
        app.grid_forget(widgets)
        return app.selectTodos()