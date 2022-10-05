import sqlite3

import app

conn = sqlite3.connect('todo.db')

class Delete:

    def __init__(self, id):
        
        cur = conn.cursor()

        sql = """DELETE FROM tbl_Todo WHERE id = ?"""

        cur.execute(sql, id)
        conn.commit()

        app.selectTodos()
