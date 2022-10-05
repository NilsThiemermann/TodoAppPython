from tkinter import *

import app

widgets = []

class Menu:
    def __init__(self, master):
        self.menuFrame = Frame(master)
        self.menuFrame.pack()

        self.selectTodosBtn = Button(master, text="Show Todos", command=self.selectTodos)
        self.createTodosBtn = Button(master, text="Create Todo", command=self.createTodos)

        self.selectTodosBtn.pack()
        self.createTodosBtn.pack()

        widgets.append(self.menuFrame)
        widgets.append(self.selectTodosBtn)
        widgets.append(self.createTodosBtn)

    def selectTodos(self):
        #remove the widgets from the frame
        #print(widgets)
        app.forget(widgets)

        return app.selectTodos()

    def createTodos(self):
        #remove the widgets from the frame
        app.forget(widgets)
        
        return app.createTodos()