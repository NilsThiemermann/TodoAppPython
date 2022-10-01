from tkinter import *
import sqlite3

import app

class Select:
    def __init__(self, master):
        conn = app.conn
        cur = conn.cursor()

        selected = cur.execute("""SELECT * FROM view_Todo""")

        print(selected)