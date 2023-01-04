import sys
from settings import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QToolBar, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

# global variables
app = QApplication(sys.argv)
app.webEngineView = QWebEngineView()
app.addressBar = QLineEdit()

def updateAddressBar(address):
    app.addressBar.setText(address.toString())

def back():
    app.webEngineView.back()

def forward():
    app.webEngineView.forward()

def stop():
    app.webEngineView.stop()

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
#     window.setStyleSheet(STYLE_SHEET)
    window.show()
    window.setWindowTitle("Py Browser")
    window.setWindowIcon(QIcon("icons/planet.png"))
    window.setGeometry(50, 50, WIDTH, HEIGHT)
    toolbar = QToolBar()
    window.addToolBar(toolbar)

    # adding back button
    backButton = QPushButton()
    backButton.setIcon(QIcon("icons/arrowLeft.png"))
    backButton.setIconSize(QSize(ICON_SIZE, ICON_SIZE))
    backButton.clicked.connect(back)  # call the back function when clicked
    toolbar.addWidget(backButton)

    # adding forward button
    forwardButton = QPushButton()
    forwardButton.setIcon(QIcon("icons/arrowRight.png"))
    forwardButton.setIconSize(QSize(ICON_SIZE, ICON_SIZE))
    forwardButton.clicked.connect(forward)  # call the forward function when clicked
    toolbar.addWidget(forwardButton)

    # adding reload button
    reloadButton = QPushButton()
    reloadButton.setIcon(QIcon("icons/reload.png"))
    reloadButton.setIconSize(QSize(ICON_SIZE, ICON_SIZE))
    reloadButton.clicked.connect(reload)  # call the reload function when clicked
    toolbar.addWidget(reloadButton)

    # adding home button
    homeButton = QPushButton()
    homeButton.setIcon(QIcon("icons/home.png"))
    homeButton.setIconSize(QSize(ICON_SIZE, ICON_SIZE))
    homeButton.clicked.connect(home)
    toolbar.addWidget(homeButton)

    # adding address line
    app.addressBar.setFont(QFont(FONT, ADDRESS_BAR_FONT_SIZE))
    app.addressBar.setText(HOME)
    app.addressBar.returnPressed.connect(search)  # call search on return key
    toolbar.addWidget(app.addressBar)

    # adding search button
    searchButton = QPushButton()
    searchButton.setIcon(QIcon("icons/magnifier.png"))
    searchButton.setIconSize(QSize(ICON_SIZE, ICON_SIZE))
    searchButton.clicked.connect(search)  # call the search function when clicked
    toolbar.addWidget(searchButton)

    # adding web page and loading it
    window.setCentralWidget(app.webEngineView)
    app.webEngineView.load(QUrl(app.addressBar.text()))

    # adding event to change addressBar text when url address of browswer changed
    app.webEngineView.urlChanged.connect(updateAddressBar)
    app.exec_()

main()
