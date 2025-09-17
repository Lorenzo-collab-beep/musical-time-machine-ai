Musical Time Machine AI is a Python UI program that asks Gemini AI to generate a list of songs based on a specified country and date, and automatically creates a playlist in your Spotify account.

HOW TO ENABLE SPOTIFY APIs ⬇️

🎵 Spotipy Integration Guide
1. Install Spotipy

First, install the library via pip:

pip install spotipy

2. Register a Spotify App

You need Spotify credentials:

Go to Spotify Developer Dashboard

Log in with your Spotify account.

Create a new app.

Copy:

Client ID

Client Secret

Set a Redirect URI (e.g. http://localhost:8888/callback).

Add this URI in your app settings.

3. Authentication with Spotipy

Spotipy uses OAuth2 to authenticate.
Here’s a simple example:

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    redirect_uri="http://localhost:8888/callback",
    scope="user-read-playback-state user-modify-playback-state"
))

Example: get current user info
user = sp.current_user()
print(user["display_name"])


👉 The first time you run this, Spotipy will open a browser window asking you to log into Spotify and authorize the app.
After that, it saves your credentials in a hidden file: .cache.

4. Using the .cache File

Spotipy creates a .cache file in your working directory.

It stores the access token and refresh token.

This means you don’t need to log in again every time.

If you delete the file, you’ll be asked to re-authenticate.

⚠️ Do not share or commit this file to GitHub – it contains sensitive tokens.
