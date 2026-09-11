from userinputs import artist_name_input, song_chosen, artist_chosen
from music import get_music_names
from play import play_audio
from playlist import get_playlist
from favlist import get_favlist
from db import Musicdb


def music_names(name=None):

    num = 1
    if name is None:
        name = artist_name_input()
    music = get_music_names(name)
    if not music:
        print("No artist found.")
        return False
    else:
        for track in music:
            print(f"{num}-{track['title']}\n {track['artist']}")
            num += 1
        size = len(music)
        choice = song_chosen(size)
        return music[choice - 1]["title"], music[choice - 1]["artist"]


def music_play_manager(name=None):

    if name is None:
        song = music_names()
    else:
        song = music_names(name)
    if not song:
        return False

    return play_audio(*song)


def main_menu():
    while True:
        print("+++++++++++++++++++++++++++++++++++++++++++++++")
        print("1- Search for an artist and play a song")
        print("2- play a song by name")
        print("3- playlist")
        print("4- Favorites Artists ")
        print("5- Exit")
        print("+++++++++++++++++++++++++++++++++++++++++++++++")
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                if music_play_manager():
                    continue
            case "2":
                song_name = input("Enter the name of the song: ")
                if play_audio(song_name):
                    continue

            case "3":
                playlist = get_playlist()
                i = 1
                for song in playlist:

                    print(f"{i}- {song}")
                    i += 1

                if (song_number := song_chosen(len(playlist))) == 0:
                    continue
                play_audio(playlist[song_number - 1])

            case "4":
                artists = get_favlist()
                i = 1
                for artist in artists:
                    print(f"{i}- {artist}")
                    i += 1
                if (artist_number := artist_chosen(len(artists))) == 0:
                    continue
                if music_play_manager(artists[artist_number - 1]):
                    continue

            case "5":
                print("Exiting...")
                break
            case _:
                print("Invalid choice. Please try again.")


def main():
    main_menu()
    Musicdb.closing()


if __name__ == "__main__":
    main()
