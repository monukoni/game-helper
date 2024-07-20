import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect('db/dbd.db')
        self.cursor = self.connection.cursor()

    def get_tips(self) -> list:
        db_returned = self.cursor.execute("SELECT text FROM tips").fetchall()
        return_list = list()
        for i in db_returned:
            return_list.append(i[0])
        return return_list
