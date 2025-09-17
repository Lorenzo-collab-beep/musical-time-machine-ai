from google import genai
from env import *


def get_song_list_by_gemini(playlist_len : str, country_name : str, moth : str, year: str) -> list:

    # optimize the prompt to make sure you can get an output you can handle correctly
    prompt = {
        f"Give me a list of the {playlist_len} most relevant or popular songs that were on the radio in {country_name} around {moth} {year}."
        f"Make sure all songs and artists are **real and actually exist**."
        f"Present the response as a list of songs, each new line must contain only the 'Song Title'."
    }

    client = genai.Client(api_key=GEMINI_API_KEY)

    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=f"{prompt}"
    )

    print(f"Gemini response:\n\n{response.text}\n")

    songs = [line.strip() for line in response.text.strip().splitlines()]

    return songs
