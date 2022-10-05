from tkinter import *
import sqlite3

import Menu
import CreateTodos
import SelectTodos
import DeleteTodo
import EditTodo

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

def deleteTodo(id):
    return DeleteTodo.Delete(id)

def editTodo():
    return EditTodo.Edit()

def forget(widgets):
    for widget in widgets:
        widget.forget()

def grid_forget(widgets):
    for widget in widgets:
        widget.grid_forget()

menu = Menu.Menu(root)

conn.commit()

conn.close()

root.mainloop()