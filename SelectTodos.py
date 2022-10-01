from tkinter import *
import sqlite3

import app

conn = sqlite3.connect('todo.db')

class Select:

    def __init__(self, master):
        
        cur = conn.cursor()

        cur.execute("""SELECT * FROM view_Todo""")
        selected = cur.fetchall()

        total_rows = len(selected)
        total_columns = len(selected[0])

        print(selected)

        for i in range(total_rows):
            for j in range(total_columns):
                
                self.e = Entry(master, width=20, fg='black', font=('Arial', 16, 'bold'))

                self.e.grid(row=i, column=j)
                self.e.insert(END, selected[i][j])

    def createTodos(self):
        #remove the widgets from the frame
        #app.forget()

        return app.createTodos()