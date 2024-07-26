import sqlite3




class Database:
    def __init__(self):
        self.connection = sqlite3.connect('db/game.db')
        self.cursor = self.connection.cursor()

    def get_tips(self, game_id: int) -> list:
        db_returned = self.cursor.execute(f"SELECT text FROM game_tips WHERE game_id={game_id}").fetchall()
        return_list = list()
        for i in db_returned:
            return_list.append(i[0])
        return return_list

    def insert_tips(self, game_id,tips: str):
        self.cursor.execute(f'INSERT INTO "main"."game_tips" ("game_id", "text") VALUES({game_id}, "{tips}");')
        self.connection.commit()

    def get_games(self) -> list:
        db_returned = self.cursor.execute("SELECT * FROM game").fetchall()
        return db_returned

    def insert_notes(self, game_id, notes: str):
        self.cursor.execute(f'INSERT INTO "main"."user_notes"("game_id", "text") VALUES ({game_id}, "{notes}");')
        self.connection.commit()

    def get_notes(self, game_id: int) -> list:
        db_returned = self.cursor.execute(f"SELECT text from user_notes WHERE game_id = {game_id}").fetchall()
        return_list = list()
        for i in db_returned:
            return_list.append(i[0])
        return return_list
