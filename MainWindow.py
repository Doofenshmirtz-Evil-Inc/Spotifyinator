# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(484, 371)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.playlistView = QtWidgets.QListView(self.centralWidget)
        self.playlistView.setAcceptDrops(True)
        self.playlistView.setProperty("showDropIndicator", True)
        self.playlistView.setDragDropMode(QtWidgets.QAbstractItemView.DropOnly)
        self.playlistView.setAlternatingRowColors(True)
        self.playlistView.setUniformItemSizes(True)
        self.playlistView.setObjectName("playlistView")
        self.verticalLayout.addWidget(self.playlistView)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.currentTimeLabel = QtWidgets.QLabel(self.centralWidget)
        self.currentTimeLabel.setMinimumSize(QtCore.QSize(80, 0))
        self.currentTimeLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.currentTimeLabel.setObjectName("currentTimeLabel")
        self.horizontalLayout_4.addWidget(self.currentTimeLabel)
        self.timeSlider = QtWidgets.QSlider(self.centralWidget)
        self.timeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.timeSlider.setObjectName("timeSlider")
        self.horizontalLayout_4.addWidget(self.timeSlider)
        self.totalTimeLabel = QtWidgets.QLabel(self.centralWidget)
        self.totalTimeLabel.setMinimumSize(QtCore.QSize(80, 0))
        self.totalTimeLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.totalTimeLabel.setObjectName("totalTimeLabel")
        self.horizontalLayout_4.addWidget(self.totalTimeLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.previousButton = QtWidgets.QPushButton(self.centralWidget)
        self.previousButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/control-skip-180.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previousButton.setIcon(icon)
        self.previousButton.setObjectName("previousButton")
        self.horizontalLayout_5.addWidget(self.previousButton)

# surgery
        # self.ppButton = QtWidgets.QPushButton(self.centralWidget)
        # self.ppButton.setText("")
        # icon1 = QtGui.QIcon()
        # icon1.addPixmap(QtGui.QPixmap("images/control.png"),
        #                 QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.ppButton.setIcon(icon1)
        # self.ppButton.setCheckable(True)


        self.playButton = QtWidgets.QPushButton(self.centralWidget)
        self.playButton.setCheckable(True)
        self.playButton.setText("")
        icon1 = QtGui.QIcon()
        # switched playbutton to look like paused as default cause theres only one button, we can switch it back when it works when music isnt playing when prgm is run
        icon1.addPixmap(QtGui.QPixmap("images/control-pause.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playButton.setIcon(icon1)
        self.playButton.setObjectName("playButton")
        self.horizontalLayout_5.addWidget(self.playButton)

<<<<<<< HEAD

        self.pauseButton = QtWidgets.QPushButton(self.centralWidget)
        self.pauseButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/control-pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pauseButton.setIcon(icon2)
        self.pauseButton.setObjectName("pauseButton")
        self.horizontalLayout_5.addWidget(self.pauseButton)
=======
        # GOT RID OF THE PAUSE BTN

        # self.pauseButton = QtWidgets.QPushButton(self.centralWidget)
        # self.pauseButton.setText("")
        # icon2 = QtGui.QIcon()
        # icon2.addPixmap(QtGui.QPixmap("images/control-pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.pauseButton.setIcon(icon2)
        # self.pauseButton.setObjectName("pauseButton")
        # self.horizontalLayout_5.addWidget(self.pauseButton)
>>>>>>> d492c55bad94297c814a565b788747488457d983
        
        self.nextButton = QtWidgets.QPushButton(self.centralWidget)
        self.nextButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/control-skip.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextButton.setIcon(icon4)
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout_5.addWidget(self.nextButton)
        self.viewButton = QtWidgets.QPushButton(self.centralWidget)
        self.viewButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/spotifyinator.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.viewButton.setIcon(icon5)
        self.viewButton.setCheckable(True)
        self.viewButton.setObjectName("viewButton")
        self.horizontalLayout_5.addWidget(self.viewButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/speaker-volume.png"))
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.volumeSlider = QtWidgets.QSlider(self.centralWidget)
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setProperty("value", 100)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setObjectName("volumeSlider")
        self.horizontalLayout_5.addWidget(self.volumeSlider)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 484, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.open_file_action = QtWidgets.QAction(MainWindow)
        self.open_file_action.setObjectName("open_file_action")
        self.menuFile.addAction(self.open_file_action)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Spotifyinator"))
        MainWindow.setWindowIcon(QtGui.QIcon("images/spotifyinator.png"))
        self.currentTimeLabel.setText(_translate("MainWindow", "0:00"))
        self.totalTimeLabel.setText(_translate("MainWindow", "0:00"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.open_file_action.setText(_translate("MainWindow", "Open file..."))
