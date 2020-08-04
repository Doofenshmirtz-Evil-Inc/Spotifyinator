import spotipy
from spotipy.oauth2 import SpotifyOAuth
from secrets import CLIENT_ID, CLIENT_SECRETS, USERNAME
import json

from TimeMachine import convert

scope = 'user-read-playback-state'
token = spotipy.util.prompt_for_user_token(USERNAME, scope, client_id=CLIENT_ID,
                                        client_secret=CLIENT_SECRETS, redirect_uri='https://github.com/TongueDaddy')


# sex time
if token:
    sp = spotipy.Spotify(auth=token)
    #results = sp.currently_playing()
    current = sp.current_playback()
    with open('jason.json', 'w') as outfile:
        json.dump(current, outfile)

    # print(currentTrack['uri'] + ' ' + currentArtist['uri'])
    currentTrack = current['item']
    currentArtist = current['item']['artists'][0]
    currentAlbum = current ['item']['album']
    progressTime = (round(current['progress_ms']/1000))
    durationTime = (round(current['item']['duration_ms']/1000))
    albumCover = current ['item']['album']['images'][0]
    print('Zack is now playing' + ' ' + currentTrack['name'])
    print('by'+ ' ' + currentArtist['name'])
    print('on'+ ' ' + currentAlbum['name'])
    print(convert(progressTime) + ' ' + '---' + ' ' + convert(durationTime))
    print(albumCover['url'])