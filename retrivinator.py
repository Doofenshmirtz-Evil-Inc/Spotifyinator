import spotipy
from spotipy.oauth2 import SpotifyOAuth
from secrets import CLIENT_ID, CLIENT_SECRETS, USERNAME
import json

from timemachininator import convert

scope = 'user-read-playback-state user-modify-playback-state'
token = spotipy.util.prompt_for_user_token(USERNAME, scope, client_id=CLIENT_ID,
                                        client_secret=CLIENT_SECRETS, redirect_uri='https://github.com/TongueDaddy')

# sex time
if token:
    sp = spotipy.Spotify(auth=token)
    #results = sp.currently_playing()
    #add shuffle state, volume %, repeat state
    current = sp.current_playback()
    isPlaying = current['is_playing']

    if isPlaying is not True:
        input('hey turn on the music idiothead')
        
    if current is None:
        print('hey we dont exist :O')
        input('say something when you are playing otherwise ima just chill: ') 

    with open('jason.json', 'w') as outfile:
        json.dump(current, outfile)

    currentTrack = current['item']
    currentArtist = current['item']['artists'][0]
    currentAlbum = current ['item']['album']
    progressTime = (round(current['progress_ms']/1000))
    durationTime = (round(current['item']['duration_ms']/1000))
    albumCover = current ['item']['album']['images'][0]
    volume = current['device']['volume_percent']
    isShuffle = current['shuffle_state']
    isRepeat = current['repeat_state']
    print('Zack is now playing' + ' ' + currentTrack['name'])
    print('by'+ ' ' + currentArtist['name'])
    print('on'+ ' ' + currentAlbum['name'])
    print(convert(progressTime) + ' ' + '---' + ' ' + convert(durationTime))
    print(albumCover['url'])
    print('at' + ' ' + str(volume))
    print('shuffle=' + str(isShuffle) + ' ' + 'repeat=' + str(isRepeat))
