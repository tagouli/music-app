import vlc
import time
import yt_dlp
import sys
import threading
import inputimeout


def get_audio_url(name):
    ytdl_opts = {
        "format": "bestaudio/best",
        "quiet": True,
    }
    try:
        with yt_dlp.YoutubeDL(ytdl_opts) as ytdl:
            info = ytdl.extract_info(f"ytsearch: {name}", download=False)
            result = info["entries"][0]
            audio_url, audio_title = result["url"], result["title"]
            return audio_url, audio_title
    except yt_dlp.utils.DownloadError as e:
        sys.exit(f"Error extracting audio URL: {e}")
    except yt_dlp.utils.ExtractorError as e:
        sys.exit(f"Error extracting audio URL: {e}")


def play_audio(namesong):
    url, title = get_audio_url(namesong)
    print(f"\n🎵 Now Playing: {title}")
    print("[p] Pause/Resume | [q] Quit")
    try:
        player = vlc.MediaPlayer(url)
        player.play()
        time.sleep(0.5)
        input_thread = threading.Thread(
            target=user_input_song_control, args=(player,), daemon=True
        )
        input_thread.start()

        while player.get_state() in [
            vlc.State.Opening,
            vlc.State.Playing,
            vlc.State.Buffering,
            vlc.State.Paused,
        ]:

            time.sleep(1)
        return True

    except vlc.VLCException as e:
        sys.exit(f"Error: {e}")


def user_input_song_control(player):

    while True:
        try:
            user_input = inputimeout.inputimeout(prompt="", timeout=10)
        except inputimeout.TimeoutOccurred:
            continue
        if user_input == "p":
            player.pause()

            if player.get_state() == vlc.State.Paused:
                print("Resumed")
            else:
                print("Paused")
        elif user_input == "q":
            print("Stopping the song...")
            player.stop()
            break
