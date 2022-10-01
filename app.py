from tkinter import *
import sqlite3

import Menu
import CreateTodos
import SelectTodos

root = Tk()
root.title("Todo - App")

# Create a database or connect to one
conn = sqlite3.connect('todo.db')

cur = conn.cursor()

#Create the Tables in the DB
sqlFile = open("dbScript.sql")
sqlStr = sqlFile.read()
cur.executescript(sqlStr)

def selectTodos():
    return SelectTodos.Select(root)

def createTodos():
    return CreateTodos.Create(root)

def forget(widgets):
    for widget in widgets:
        widget.forget()

menu = Menu.Menu(root)

conn.commit()

conn.close()

root.mainloop()