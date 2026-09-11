from db import Musicdb


def playlist_save(title, artist):
    return Musicdb.insert_new_song(title, artist)


def get_playlist():
    rows = Musicdb.read_from_db_playlist_table()

    songs = []
    for row in rows:
        if not row[1]:
            songs.append(row[0])
        else:
            songs.append(f"{row[0]} by {row[1]}")
    return songs
