import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

user_date = input("which year do you want to travel to? type date in this format yyyy-mm-dd: ")
URL = f"https://www.billboard.com/charts/hot-100/{user_date}/"

response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html,"html.parser")
titles = soup.select("li h3")
songs_list = []
for title in titles[:100]:
    songs_list.append(title.getText().strip())
# print(songs_list)
#spotify authentication
Client_ID = "YOUR_CLIENT_ID"
Client_Secret = "YOUR_CLIENT_SECRET_KEY"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=Client_ID,
        client_secret=Client_Secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
song_uris = []
year = user_date.split("-")[0]
for song in songs_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{user_date} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
# titles = soup.findAll(name="h3", id="title-of-a-story")
# print(titles)
# for title in titles:
#     print(f"{title.getText().strip()}\n")


