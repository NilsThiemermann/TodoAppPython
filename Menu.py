from tkinter import *

import app


class Menu:
    def __init__(self, master):
        self.menuFrame = Frame(master)
        self.menuFrame.pack()

        self.selectTodosBtn = Button(master, text="Show Todos", command=self.selectTodos)
        self.createTodosBtn = Button(master, text="Create Todo", command=self.createTodos)

        self.selectTodosBtn.pack()
        self.createTodosBtn.pack()

    def selectTodos(self):
        #self.menuFrame.destroy()
        return app.selectTodos()

    def createTodos(self):
        #self.menuFrame.destroy()
        return app.createTodos()