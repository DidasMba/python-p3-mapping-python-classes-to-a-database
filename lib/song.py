from config import CONN, CURSOR

class Song:
    def __init__(self, name, album):
        self.name = name
        self.album = album


def create_table(cls):
    sql = """
     CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
    """

    CURSOR.execute(sql)

  def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.album))
        # Additional code to retrieve the last inserted ID and set it to self.id
        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM songs").fetchone()[0]  