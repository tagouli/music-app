# Music App

A Python command-line music application that lets users:

- Search for an artist
- Browse their popular songs and play song from the list
- Search and play songs
- Save songs to a playlist
- Save artists to favorites
- Play songs from the playlist
- Browse favorite artists

## Features

* Search for an artist using the Deezer API
* Display the artist's popular songs
* Select and play a song from the search results
* Search for a song by name and play it
* Save songs to a local SQLite playlist
* Save artists to a local favorites list
* Browse and play saved songs from the playlist
* Browse favorite artists and search their popular songs
* Control playback with pause/resume and stop


## Technologies

- Python
- Deezer API
- yt-dlp
- VLC
- SQLite
- requests

## How it works

the user can search for their fav arists and get their popular songs and play it , with option to save the artist to favorite and save song to to playlist for future use .

## Installation

pip install -r requirements.txt then python main.py 


## Usage
- Option 1 : Search for artist poplar songs and play a song from the list 
- Option 2 : Search for a song by name and play it 
- Option 3 : Play song from playlist
- Option 4 : Get artist from favorites and search and play their popular songs
- Option 5 : exit program



## Project Structure

```text
music-app/
├── main.py          # Main entry point and application menu
├── music.py         # Deezer API requests and music search
├── play.py          # Audio searching, playback, and playback controls
├── db.py            # SQLite database setup and database operations
├── playlist.py      # Playlist-related functions
├── favlist.py       # Favorite artist-related functions
├── userinputs.py    # User input and validation functions
├── menu.py          # Playback menu display
├── requirements.txt # Project dependencies
├── .gitignore       # Files ignored by Git
└── README.md        # Project documentation

```

## Future plans

- GUI
- Packaging
- Tests