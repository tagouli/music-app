from userinputs import artist_name_input
from music import get_music_names


def main():
    
    print("+++++++++++++++++++++++++++++++++++++++++++++++")
    
    while True:
        if music_names():
            break


def music_names():
    name = artist_name_input()
    music = get_music_names(name)
    if not music:
        print("No artist found.")
        return False
    else:
        print(*music, sep="\n")
        return True


if __name__ == "__main__":
    main()
