from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5 import QtCore, QtWidgets
from MainWindow import Ui_MainWindow
import spotipy
from secrets import CLIENT_ID, CLIENT_SECRETS, USERNAME
import json
import os
import keyboard
from timemachininator import convert


def getSp():
    scope = 'user-read-playback-state user-modify-playback-state'
    token = spotipy.util.prompt_for_user_token(USERNAME, scope, client_id=CLIENT_ID,
                                        client_secret=CLIENT_SECRETS, redirect_uri='https://github.com/TongueDaddy')
    return spotipy.Spotify(auth=token)

sp = getSp()

def hhmmss(ms):
    # s = 1000
    # m = 60000
    # h = 360000
    h, r = divmod(ms, 36000)
    m, r = divmod(r, 60000)
    s, _ = divmod(r, 1000)
    return ("%d:%02d:%02d" % (h, m, s)) if h else ("%d:%02d" % (m, s))


class ViewerWindow(QMainWindow):
    
    def closeEvent(self, e):
        # Emit the window state, to update the viewer toggle button.
        self.state.emit(False)

class SpotifyPlayer(QMainWindow):
    
    durationChanged = pyqtSignal()
    positionChanged = pyqtSignal()
    # zadk move this to the mainwindow class!!!!!!!!!!!!!!!! then pass it as a param

    def play(self, playButton):
        print('play called')
        sp.start_playback()
        icon2 = QIcon()
        icon2.addPixmap(QPixmap("images/control-pause.png"), QIcon.Normal, QIcon.Off)
        playButton.setIcon(icon2)

    def pause(self, pauseButton):
        print('pause called')
        sp.pause_playback()
        icon1 = QIcon()
        icon1.addPixmap(QPixmap("images/control.png"),
                        QIcon.Normal, QIcon.Off)
        pauseButton.setIcon(icon1)
        # basically you wanna find out if u can pass any data thru signals and if so how yes

        # lambda is a function but smoler yeah u dont name it
# that sounds like a good idea try that
    def setVolume(self, volume):
        print('setVolume called')

    def next(self):
        print('next called')
        sp.next_track()
    
    def prev(self):
        print('prev called')
        sp.previous_track() # yo zack i moved the functions here cuz they were one liners

    def setPosition(self):
        print('setPosition called')

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.player = SpotifyPlayer()

        # Connect control buttons/slides for media player.
        # these are connect not normal calls
        # self.playButton.pressed.connect(self.player.play)
        #self.pauseButton.pressed.connect(self.player.pause)
        self.volumeSlider.valueChanged.connect(self.player.setVolume)


        #find a way to get the checked button to run the play()
        if self.playButton.isChecked():
            self.playButton.connect(lambda: self.player.play(window.playButton))
        #^play to pause
        else:
            self.pauseButton.pressed.connect(lambda: self.player.pause(window.pauseButton))
        #^pasue to play
        

        
        self.nextButton.pressed.connect(self.player.next)
        self.previousButton.pressed.connect(self.player.prev)

        self.player.durationChanged.connect(self.update_duration)
        self.player.positionChanged.connect(self.update_position)
        self.timeSlider.valueChanged.connect(self.player.setPosition)

        self.show()
        #clicky button for the play pause
    # this might just actually work 1 sec
        # self.model.layoutChanged.emit()

        # # If not playing, seeking to first of newly added + play.
        # if self.player.state() != QMediaPlayer.PlayingState:
        #     self.player.play()

    
    def update_duration(self, duration):
        print("!", duration)
        print("?", self.player.duration())

        self.timeSlider.setMaximum(duration)

        if duration >= 0:
            self.totalTimeLabel.setText(hhmmss(duration))

    def update_position(self, position):
        if position >= 0:
            self.currentTimeLabel.setText(hhmmss(position))

        # Disable the events to prevent updating triggering a setPosition event (can cause stuttering).
        self.timeSlider.blockSignals(True)
        self.timeSlider.setValue(position)
        self.timeSlider.blockSignals(False)


    def toggle_viewer(self, state):
        if state:
            self.viewer.show()
        else:
            self.viewer.hide()

    def erroralert(self, *args):
        print(args)


if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("spotifyinator")
    app.setStyle("Fusion")

    # Fusion dark palette from https://gist.github.com/QuantumCD/6245215.
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)
    app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

    window = MainWindow()
    app.exec_()
