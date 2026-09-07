import requests
import sys


def get_artist_id(name):

    try:
        name = name.strip()
        response = requests.get(f"https://api.deezer.com/search", params={"q": name})
        response.raise_for_status()
        data = response.json()
       
        if data["total"] == 0:
            return None
        
        artist_id = data["data"][0]["artist"]["id"]

        return artist_id
    except KeyError as e:
        sys.exit(f"Error: {e}")
    except requests.HTTPError as e:
        sys.exit(f"API error: {e}")
    except requests.ConnectionError:
        sys.exit("Connection error.")


def get_music_names(name):
    try:
        artist_id = get_artist_id(name)
        if artist_id is None:
            return []
        response = requests.get(
            f"https://api.deezer.com/artist/{artist_id}/top?limit=10"
        )
        response.raise_for_status()
        data = response.json()
        music_names = [track["title"] for track in data["data"]]
        return music_names
    except requests.HTTPError as e:
        sys.exit(f"HTTP error: {e}")
    except requests.ConnectionError:
        sys.exit("Connection error.")
