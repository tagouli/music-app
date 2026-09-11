import sqlite3

TIMEOUT = 20


class Musicdb:
    conn = sqlite3.connect("music.db", timeout=TIMEOUT)
    cursor = conn.cursor()  # create a pointer
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS playlist (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL,artist TEXT NOT NULL,UNIQUE(name,artist))"
    )
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS favorites (id INTEGER PRIMARY KEY AUTOINCREMENT, artist TEXT NOT NULL , UNIQUE(artist))"
    )

    # SONG
    @classmethod
    def insert_new_song(cls, title, artist):
        try:
            print("SAVING SONG")
            song = (title, artist)
            cls.cursor.execute("INSERT INTO playlist (name,artist) VALUES (?,?)", song)
            return True

        except sqlite3.IntegrityError:
            print("Save Failed : Song already exist in playlist")
            return False

    @classmethod
    def read_from_db_playlist_table(cls):
        cls.cursor.execute("SELECT name,artist FROM playlist")
        all_rows = cls.cursor.fetchall()
        return all_rows

    # ARTIST

    @classmethod
    def insert_new_artist(cls, artist_name):
        try:
            print("SAVING ARTIST")
            artist = (artist_name,)
            cls.cursor.execute("INSERT INTO favorites (artist) VALUES (?)", artist)
            return True

        except sqlite3.IntegrityError:
            print("Save Failed : artist already exist in favorites")
            return False

    @classmethod
    def read_fav_artists(cls):
        cls.cursor.execute("SELECT artist FROM favorites")
        all_rows = cls.cursor.fetchall()
        return all_rows

    @classmethod
    def commit(cls):
        print("Saving ")
        cls.conn.commit()

    @classmethod
    def closing(cls):
        cls.conn.close()
        cls.cursor.close()
