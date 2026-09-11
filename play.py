import vlc
import time
import yt_dlp
import sys
import threading
import inputimeout
from menu import song_menu
from playlist import playlist_save
from favlist import fav_save, commit
from music import get_artist_name

song_save = False
end = False
artist_save = False


def get_audio_url(name, artist):
    ytdl_opts = {
        "format": "bestaudio/best",
        "quiet": True,
    }
    try:
        with yt_dlp.YoutubeDL(ytdl_opts) as ytdl:

            info = ytdl.extract_info(
                f"ytsearch: '{name}' by '{artist}'", download=False
            )
            result = info["entries"][0]
            audio_url, audio_title, audio_duration = (
                result["url"],
                result["title"],
                result["duration"],
            )

            artist = get_artist_name(name)

            return audio_url, audio_title, audio_duration, artist

    except yt_dlp.utils.DownloadError as e:
        sys.exit(f"Error extracting audio URL: {e}")
    except yt_dlp.utils.ExtractorError as e:
        sys.exit(f"Error extracting audio URL: {e}")


def play_audio(song_title, song_artist=""):
    global song_save, end, artist_save
    song_save = False
    end = False
    artist_save = False
    url, title, duration, song_artist = get_audio_url(song_title, song_artist)
    print(f"\n🎵 Now Playing: {title}")
    print("Song Artist is ", song_artist)

    song_menu()

    try:
        player = vlc.MediaPlayer(url)
        player.play()
        time.sleep(0.5)
        input_thread = threading.Thread(
            target=user_input_song_control, args=(player, duration), daemon=True
        )
        input_thread.start()

        while player.get_state() in [
            vlc.State.Opening,
            vlc.State.Playing,
            vlc.State.Buffering,
            vlc.State.Paused,
        ]:

            time.sleep(1)
        if song_save:
            if playlist_save(song_title, song_artist):
                if artist_save:
                    fav_save(song_artist)

        elif artist_save:
            fav_save(song_artist)

        commit()

        end = True
        return True

    except vlc.VLCException as e:
        sys.exit(f"Error: {e}")


def user_input_song_control(player, duration):

    while True:
        try:
            user_input = inputimeout.inputimeout(
                prompt="", timeout=(duration * 25) / 100
            )
        except inputimeout.TimeoutOccurred:
            if not end:
                continue
            break
        if user_input == "p":
            player.pause()

            if player.get_state() == vlc.State.Paused:
                print("Resumed")
            else:
                print("Paused")
        elif user_input == "s":
            global song_save
            song_save = True
        elif user_input == "a":
            global artist_save
            artist_save = True
        elif user_input == "q":
            print("Stopping the song...")
            player.stop()
            break
