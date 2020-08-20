import os
import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

import PySimpleGUI as sg
import requests
import io
from PIL import Image,ImageTk

from secrets import CLIENT_ID, CLIENT_SECRETS, USERNAME

# Check Vars from secrets.py
# print(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URL, USERNAME)

scope = "user-read-playback-state user-modify-playback-state"

token = spotipy.util.prompt_for_user_token(USERNAME, scope, client_id=CLIENT_ID,
                                        client_secret=CLIENT_SECRETS, redirect_uri='https://github.com/TongueDaddy')
sp = spotipy.Spotify(auth=token)

current = sp.current_playback()

currentTrack = current['item']
currentArtist = current['item']['artists'][0]
currentAlbum = current ['item']['album']
progressTime = (round(current['progress_ms']/1000))
durationTime = (round(current['item']['duration_ms']/1000))
albumCover = current ['item']['album']['images'][0]

print('\n' + 'Aidan is now playing: ' + currentTrack['name'] + ' by ' + currentArtist['name'] + ' from ' + currentAlbum['name'] + '\n')
line1 = str(currentTrack['name'] + ' - ' + currentArtist['name'] + ' - ' + currentAlbum['name'])

def get_img_data(f, maxsize=(800, 640), first=False):
# Generate image data using PIL
    img = Image.open(f)
    img.thumbnail(maxsize)
    if first:                     # tkinter is inactive the first time
        bio = io.BytesIO()
        img.save(bio, format="PNG")
        del img
        # print(bio.getvalue())
        return bio.getvalue()
    return ImageTk.PhotoImage(img)

albumURL = albumCover['url']
response = requests.get(albumURL,stream=True)
image_data = get_img_data(response.raw,first=True)
image_elem = sg.Image(data=image_data)

sg.theme('DarkTeal2')
layout = [  [sg.Text(text='Spotifyinator v0.1', size=(15,1)), sg.Text(USERNAME)],
            [sg.Text(line1)],
            [image_elem],
            [sg.Button('play/pause')],
            # [sg.Image(r'C:\Users\Aidan\Desktop\kneeXRAY2.png')],
            [sg.Button('Ok'), sg.Button('Cancel')] ]
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

inp = input('play or pause? (pl/pa)')
if inp == 'pl':
    sp.start_playback()
if inp == 'pa  ':
    sp.pause_playback()
    # pause_playback
