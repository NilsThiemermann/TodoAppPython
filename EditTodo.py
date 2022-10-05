from tkinter import *
import sqlite3

import app

conn = sqlite3.connect('todo.db')

class Edit:

    def __init__(self, id):
        
        cur = conn.cursor()
