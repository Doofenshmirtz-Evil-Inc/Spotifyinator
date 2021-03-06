import json

import spotipy
from secrets import CLIENT_ID, CLIENT_SECRETS, USERNAME
from timemachininator import convert
import time
#fucntion tyme


# def setVolume():
#     sp.next_track()

# fucntion tyme


def Volume():
    sp.next_track()


def prevTrack():
    sp.previous_track()


def skipTrack():
    sp.next_track()


def pausePlayback():
    sp.pause_playback()


def startPlayback():
    sp.start_playback()


def getToken():
    scope = 'user-read-playback-state user-modify-playback-state'
    return spotipy.util.prompt_for_user_token(USERNAME, scope, client_id=CLIENT_ID,
                                              client_secret=CLIENT_SECRETS, redirect_uri='https://github.com/TongueDaddy')


def getInfo():
    currentTrack = current['item']
    currentArtist = current['item']['artists'][0]
    currentAlbum = current['item']['album']
    progressTime = (round(current['progress_ms']/1000))
    durationTime = (round(current['item']['duration_ms']/1000))
    albumCover = current['item']['album']['images'][0]
    volume = current['device']['volume_percent']
    isShuffle = current['shuffle_state']
    isRepeat = current['repeat_state']
    print('Zack is now playing' + ' ' + currentTrack['name'])  # track
    print('by' + ' ' + currentArtist['name'])  # artist
    print('on' + ' ' + currentAlbum['name'])  # album
    print(convert(progressTime) + ' ' + '---' +
          ' ' + convert(durationTime))  # time
    print(albumCover['url'])  # picutre url
    print('at' + ' ' + str(volume))  # how much luoud
    print('shuffle=' + str(isShuffle) + ' ' + 'repeat=' +
          str(isRepeat))  # shuffle and repeat state


if __name__ == "__main__":
    token = getToken()
    # sex time
    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.currently_playing()
        # add shuffle state, volume %, repeat state*
        current = sp.current_playback()

        if current is None or current['is_playing'] is not True:
            print('hey we dont exist :O')
            input('say something when you are playing otherwise ima just chill: ')
            sp.start_playback()

            # please start playing music when i want it to
            # then look for what song is playing

        with open('jason.json', 'w') as outfile:
            json.dump(current, outfile)

        getInfo()  # this is info going to display
        # while True:
        #     try:
        #         if keyboard.is_pressed('right arrow'):  # keyboard controls
        #             sp.next_track()
        #             pass
        #         if keyboard.is_pressed('left arrow'):
        #             sp.previous_track()
        #             pass
        #         if keyboard.is_pressed('space'):
        #             try:
        #                 sp.start_playback()
        #                 pass
        #             except:
        #                 sp.pause_playback()
        #                 pass
        #     except:
        #         print('uh oh, theres an oopsies')
        #         break
