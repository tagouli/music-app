def artist_name_input():
    name = input("Enter artist name: ").strip()
    return name


def song_chosen(size):
    while True:
        try:
            choice = int(input("Enter the number of the song you want to play: "))
            if 1 <= choice <= size:
                return choice
            else:
                print(f"Invalid choice. Please enter a number between 1 and {size}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
