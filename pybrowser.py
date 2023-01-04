import sys
from settings import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QToolBar, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage

# global variables
app = QApplication([])
app.webEngineView = QWebEngineView()
app.addressBar = QLineEdit()


def updateAddressBar():
    app.addressBar.setText(app.webEngineView.url().toString())

def back():
    app.webEngineView.back()

def forward():
    app.webEngineView.forward()

def search():
    request = app.addressBar.text()
    if request[0] == 's' or request[0] == 'S':
        request = request[1:]
        app.webEngineView.load(QUrl('https://www.google.com/search?q=' + request))
    else:
        app.webEngineView.load(QUrl(app.addressBar.text()))

def reload():
    app.webEngineView.reload()

def home():
    app.webEngineView.load(QUrl(HOME))

def main():
    window = QMainWindow()
    window.show()
    window.setWindowTitle("Py Browser")
    window.setWindowIcon(QIcon("icons/planet.png"))
    window.setGeometry(100, 50, WIDTH, HEIGHT)
    toolbar = QToolBar()
    window.addToolBar(toolbar)

    # adding back button
    backButton = QPushButton()
    backButton.setIcon(QIcon("icons/arrowLeft.png"))
    backButton.setIconSize(QSize(32, 32))
    backButton.clicked.connect(back)  # call the back function when clicked
    toolbar.addWidget(backButton)

    # adding forward button
    forwardButton = QPushButton()
    forwardButton.setIcon(QIcon("icons/arrowRight.png"))
    forwardButton.setIconSize(QSize(32, 32))
    forwardButton.clicked.connect(forward)  # call the forward function when clicked
    toolbar.addWidget(forwardButton)

    # adding reload button
    reloadButton = QPushButton()
    reloadButton.setIcon(QIcon("icons/reload.png"))
    reloadButton.setIconSize(QSize(32, 32))
    reloadButton.clicked.connect(reload)  # call the reload function when clicked
    toolbar.addWidget(reloadButton)

    # adding home button
    homeButton = QPushButton()
    homeButton.setIcon(QIcon("icons/home.png"))
    homeButton.setIconSize(QSize(32, 32))
    homeButton.clicked.connect(home)
    toolbar.addWidget(homeButton)

    # adding address line
    app.addressBar.setFont(QFont("TimesNewRoman", 14))
    app.addressBar.setText(HOME)
    app.addressBar.returnPressed.connect(search)  # call search on return key
    toolbar.addWidget(app.addressBar)

    # adding search button
    searchButton = QPushButton()
    searchButton.setIcon(QIcon("icons/magnifier.png"))
    searchButton.setIconSize(QSize(32, 32))
    searchButton.clicked.connect(search)  # call the search function when clicked
    toolbar.addWidget(searchButton)

    # adding web page and loading it
    window.setCentralWidget(app.webEngineView)
    app.webEngineView.load(QUrl(app.addressBar.text()))

    # adding event to change addressBar
    app.webEngineView.loadFinished.connect(updateAddressBar)
    app.exec_()

main()
