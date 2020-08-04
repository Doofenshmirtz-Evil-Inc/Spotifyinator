import sys
import PyQt5.QtWidgets as qt

app = qt.QApplication(sys.argv)

window = qt.QMainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.
window.setWindowTitle('Spotifyinator')
# Start the event loop.
app.exec_()
