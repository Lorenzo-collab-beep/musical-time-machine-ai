from tkinter import ttk
from ui import Window
from assets import get_countries_list
from gemini import get_song_list_by_gemini
from spotify import create_spotify_playlist

MAX_PLAYLIST_LEN = 100
DEFAULT_PLAYLIST_LEN = 20

MAX_YEAR_BASED_ON_GEMINI_INFO = 2023

# root window
window = Window()

# country label and combobox
country_label = ttk.Label(window.root(), text="Select a country:")
country_label.pack(pady=10)
country_combo = ttk.Combobox(window.root(), values=get_countries_list())
country_combo.set(get_countries_list()[0])
country_combo.pack()

# mouths label and combobox
mouths_label = ttk.Label(window.root(), text="Select a month:")
mouths_label.pack(pady=10)
mouths_combo = ttk.Combobox(window.root(), values=[
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
])
mouths_combo.set("Jan")
mouths_combo.pack()

# year label and combobox
years_label = ttk.Label(window.root(), text="Select a year:")
years_label.pack(pady=10)
years = [str(year) for year in list(range(MAX_YEAR_BASED_ON_GEMINI_INFO, 1919, -1))]
years_combo = ttk.Combobox(window.root(), values=years)
years_combo.set(MAX_YEAR_BASED_ON_GEMINI_INFO)
years_combo.pack()

# validate playlist len input
def check_playlist_len(value):
    return (value.isdigit() and int(value) < (MAX_PLAYLIST_LEN+1)) or value == ""

validate_cmd = (window.root().register(check_playlist_len), '%P')

# playlist label  len entry
playlist_label = ttk.Label(window.root(), text=f"How many song (max {MAX_PLAYLIST_LEN}):")
playlist_label.pack(pady=10)
playlist_entry = ttk.Entry(window.root(), validate="key", validatecommand=validate_cmd)
playlist_entry.insert(0, str(DEFAULT_PLAYLIST_LEN))
playlist_entry.pack()

# button callback
def button_callback():
    global wait_label
    wait_label.config(text="Asking AI ...")
    window.root().update()
    songs = get_song_list_by_gemini(playlist_entry.get(), country_combo.get(), mouths_combo.get(), years_combo.get())
    wait_label.config(text="Creating Spotify Playlist ...")
    window.root().update()
    create_spotify_playlist(songs, country_combo.get(), mouths_combo.get(), years_combo.get())
    wait_label.config(text="Done")
    window.root().update()

ttk.Button(window.root(), text="Create playlist", command=button_callback).pack(pady=30)

# wait label  len entry
wait_label = ttk.Label(window.root(), text="")
wait_label.pack(pady=5)

window.mainloop()