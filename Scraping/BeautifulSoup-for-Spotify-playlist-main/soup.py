import requests
from bs4 import BeautifulSoup
import datetime
import os
from spotipy.oauth2 import SpotifyOAuth
from spotipy.client import Spotify
from spotipy.cache_handler import CacheFileHandler


def process_artist(s: str) -> str:
    """ Returns a 'friendly' string for Spotify search engine.
    This function replaces single quotes with an empty string and removes content between parantheses,
    if any, and removes the words "Feat".

    Parameters:
        s (str): input string representing the artist name.

    Returns:
        str: processed artist name string for Spotify search engine. """
    
    out = s.replace("'", "")

    open_par = out.find("(")
    close_par = out.find(")")
    if 0 <= open_par < close_par:
        out = out.split("(")[0] + out.split(")")[1]

    out = out.split("Feat")[0]

    return out


def process_track(s: str) -> str:
    """
    Returns a 'friendly' string for Spotify search engine.
    This function replaces single quotes with an empty string, removes content between parantheses,
    if any, and removes words with an asterisk.

    Parameters:
        s (str): input string representing the track name.

    Returns:
        str: processed track name string for Spotify search engine.
    """
    
    out = s.replace("'", "")

    open_par = out.find("(")
    close_par = out.find(")")
    if 0 <= open_par < close_par:
        out = out.split("(")[0] + out.split(")")[1]

    words = out.split(" ")
    out = ""
    for w in words:
        if w.find('*') < 0:
            out = out + w + " "

    return out


def get_song_uris(client: Spotify, tracks: [str], track_artists: [str]) -> [str]:
"""
    Returns song URIs from tracks and artists names.
    This function processes the track and artist names to a 'friendly' format, searches for the track on
    Spotify and returns the corresponding URI.

    Parameters:
        client (Spotify): spotipy client instance.
        tracks ([str]): list of track names.
        track_artists ([str]): list of artist names corresponding to the tracks.

    Returns:
        [str]: list of song URIs found on Spotify.
    """

    uris = []
    for track, artist in zip(tracks, track_artists):
        processed_track = process_track(track)
        processed_artist = process_artist(artist)

        query = f"{processed_track} {processed_artist}"
        results = client.search(q=query, type="track", market="US", limit=1)
        try:
            uris.append(results["tracks"]["items"][0]["uri"])
        except IndexError:
            print(f"'{track} --- {artist}' not found.")
            print(f"{processed_track} --- {processed_artist}.")

    return uris


def get_playlist(client: Spotify, user: int, name: str) -> int:
  """
    Given a Spotify client, a user id, and a playlist name, the function returns the id of the playlist.
    If the playlist doesn't exist, it creates the playlist and returns its id.

    :param client: Instance of Spotify client.
    :param user: User id of the Spotify user.
    :param name: Name of the playlist to be created or searched for.
    :return: Id of the playlist.
    """

    playlists = spotify.user_playlists(user_id)["items"]

    for p in playlists:
        if p["name"] == name:
            return 0

    playlist = client.user_playlist_create(user=user, name=name, public=False)

    return playlist["id"]


def get_spotify_client() -> Spotify:
    """
    Returns an instance of Spotify client using environment variables for authentication.

    :return: Instance of Spotify client.
    """
    
    spotify_client_id = os.environ['SPOTIFY_CLIENT_ID']
    spotify_client_secret = os.environ['SPOTIFY_CLIENT_SECRET']
    spotify_redirect_uri = "http://localhost:8888/callback"
    spotify_scope = "playlist-modify-private playlist-read-private"  # Allows us to read and modify private playlists
    spotify_cache_handler = CacheFileHandler("./token.txt")

    return Spotify(
        auth_manager=SpotifyOAuth(
            client_id=spotify_client_id,
            client_secret=spotify_client_secret,
            redirect_uri=spotify_redirect_uri,
            scope=spotify_scope,
            cache_handler=spotify_cache_handler
        )
    )


def get_billboard_songs_artists(date_str: str) -> ([str], [str]):
    """
    Given a date string in the format 'YYYY-MM-DD', returns the list of songs and artists
    that were on the billboard top 100 chart on that date.

    :param date_str: Date string in the format 'YYYY-MM-DD'.
    :return: Tuple of lists containing the songs and artists on the billboard top 100 chart on the specified date.
    """
    
    billboard_url = "https://www.billboard.com/charts/hot-100/"
    response = requests.get(billboard_url + date_str)

    soup = BeautifulSoup(response.text, "html.parser")
    # There are a lot of trash '\n' and '\t' in raw content
    raw_titles = [t.getText() for t in soup.select("li > h3.c-title")]
    raw_artists = [artist.getText() for artist in soup.select("li > span.a-no-trucate")]

    # Get rid of those \n and \t
    processed_titles = [t.replace("\n", "").replace("\t", "") for t in raw_titles]
    processed_artists = [a.replace("\n", "").replace("\t", "") for a in raw_artists]

    return processed_titles, processed_artists


def check_date(date_str: str) -> bool:
    """
    Check if the date format is correct and if the date is less than or equal to today.
    
    Parameters:
    date_str (str): The string representation of the date in the format "YYYY-MM-DD".

    Returns:
    bool: True if the date is in the correct format and less than or equal to today, False otherwise.
    """
    
    wrong_format_msg = "Wrong date format. Must be -> YYYY-MM-DD"
    # Date to int
    try:
        ymd = [int(i) for i in date_str.split("-")]
    except ValueError:
        print(wrong_format_msg)
        return False
    # Check that we got three values
    if len(ymd) != 3:
        print(wrong_format_msg)
        return False
    # Check date format is valid
    try:
        date_obj = datetime.date(year=ymd[0], month=ymd[1], day=ymd[2])
    except ValueError as e:
        print(e)
        return False

    today = datetime.date.today()
    # A future date is not allowed
    if date_obj > today:
        print("Input date can't be higher than current date")
        return False
    # Everything is OK
    return True


if __name__ == "__main__":
    """
    Main program execution.
    Asks the user for a date, checks the date format and adds the top 100 songs from the Billboard charts to a Spotify playlist.
    """ 
    
    date = input("Enter date YYYY-MM-DD: ")
    if check_date(date):
        songs, artists = get_billboard_songs_artists(date)

        spotify = get_spotify_client()
        user_id = spotify.me()["id"]
        playlist_name = "Top 100. " + date

        playlist_id = get_playlist(spotify, user_id, playlist_name)

        if playlist_id != 0:  # Playlist didn't exist
            song_uris = get_song_uris(spotify, songs, artists)
            spotify.playlist_add_items(playlist_id, song_uris)
        else:
            print("That playlist already existed.")
