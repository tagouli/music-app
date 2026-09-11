def artist_name_input():
    name = input("Enter artist name: ").strip()
    return name


def song_chosen(size):
    while True:
        try:
            choice = int(
                input("Enter the number of the song you want to play | [0] Menu : ")
            )
            if 0 <= choice <= size:
                return choice
            else:
                print(
                    f"Invalid choice. Please enter a number between 1 and {size} or 0 ."
                )
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def artist_chosen(size):
    while True:
        try:
            choice = int(input("Enter the number of the artist | [0] Menu : "))
            if 0 <= choice <= size:
                return choice
            else:
                print(
                    f"Invalid choice. Please enter a number between 1 and {size} or 0 ."
                )
        except ValueError:
            print("Invalid input. Please enter a valid number.")
