from userinputs import artist_name_input, song_chosen
from music import get_music_names
from play import play_audio


def music_names():
    num = 1
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
        return f"{music[choice - 1]["title"]} by {music[choice - 1]["artist"]}"


def music_play_manager():
    song_name = music_names()
    if not song_name:
        return False

    return play_audio(song_name)


def main():

    print("+++++++++++++++++++++++++++++++++++++++++++++++")

    while True:
        if music_play_manager():
            break


if __name__ == "__main__":
    main()
