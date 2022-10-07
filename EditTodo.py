from tkinter import *
import sqlite3

import app

conn = sqlite3.connect('todo.db')

widgets = []

class Edit:

    def __init__(self, master, id):

        data = self.getData(id)
        self.gui(master, data)

    def getData(_, id):

        cur = conn.cursor()

        sql = """SELECT id, todo, expenditure_of_time, fk_importance, expiry_date FROM tbl_Todo WHERE id = ?"""

        cur.execute(sql, [(id)])
        data = cur.fetchone()

        return data

    def gui(self, master, data):

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

        self.btnUpdate = Button(master, text='Update', command= lambda: self.updateData(int(data[0])))
        self.btnUpdate.grid(row=5, column=2)

        print(data)

        self.e1.insert(0,(data[1]))
        self.e2.insert(0,(data[2]))
        self.e3.insert(0,(data[3]))
        self.e4.insert(0,(data[4]))
        
        widgets.append(self.e1)
        widgets.append(self.e2)
        widgets.append(self.e3)
        widgets.append(self.e4)
        widgets.append(self.btnUpdate)
    
    def updateData(self, id):

        cur = conn.cursor()

        sql = """UPDATE tbl_Todo 
        SET todo = ?,
        expenditure_of_time = ?,
        fk_importance = ?,
        expiry_date = ?
        WHERE id = ?"""

        v1 = self.e1.get()
        v2 = self.e2.get()
        v3 = self.e3.get()
        v4 = self.e4.get()

        values = [v1, v2, v3, v4, id]
        
        cur.execute(sql, values)
        conn.commit()

        app.grid_forget(widgets)
        app.selectTodos()
