import sys
from PyQt5 import QtGui, QtWidgets, QtCore, QtLocation

app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QMainWindow()
window.show()  # windows are hidden by default.
window.setWindowTitle('Spotifyinator')
window.setWindowIcon(QtGui.QIcon('spotifyinator.png'))

label = QtWidgets.QLabel("youve been thunderstruck")

# The `Qt` namespace has a lot of attributes to customise
# widgets. See: http://doc.qt.io/qt-5/qt.html
label.setAlignment(QtCore.Qt.AlignCenter)

# Set the central widget of the Window. Widget will expand
# to take up all the space in the window by default.
window.setCentralWidget(label)

# Start the event loop.
app.exec_()
