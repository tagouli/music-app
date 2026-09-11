from db import Musicdb


def fav_save(artist: str):
    if artist is None:
        return False
    print("saving artist1")
    return Musicdb.insert_new_artist(artist)


def get_favlist():
    rows = Musicdb.read_fav_artists()
    artists = []
    for row in rows:
        artists.append(row[0])

    return artists


def commit():
    Musicdb.commit()
