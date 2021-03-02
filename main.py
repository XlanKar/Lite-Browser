import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Lite Browser by XlanKar")
        self.setMinimumSize(1100, 600)
        self.showMaximized()
        self.setWindowIcon(QIcon("litebrowser.ico"))
        self.tab = QTabWidget()
        self.tab.setTabBarAutoHide(True)
        self.setCentralWidget(self.tab)
        self.navBar = QToolBar()
        self.navBar.setStyleSheet("background:#333;color:white")
        self.navBar.setFixedHeight(46)
        self.navBar.setMovable(False)
        self.addToolBar(self.navBar)
        self.backBtn = QAction("<", self)
        self.backBtn.triggered.connect(lambda: self.tab.currentWidget().back())
        self.navBar.addAction(self.backBtn)
        self.nextBtn = QAction(">", self)
        self.nextBtn.triggered.connect(lambda: self.tab.currentWidget().forward())
        self.navBar.addAction(self.nextBtn)
        self.reBtn = QAction("Reload", self)
        self.reBtn.triggered.connect(lambda: self.tab.currentWidget().reload())
        self.navBar.addAction(self.reBtn)
        self.linkBar = QLineEdit()
        self.linkBar.returnPressed.connect(self.goLink)
        self.navBar.addWidget(self.linkBar)
        self.createNewTab(QUrl("https://www.google.com"))

    def createNewTab(self, url):
        brw = QWebEngineView()
        brw.setUrl(url)
        i = self.tab.addTab(brw, "HomePage")
        brw.urlChanged.connect(lambda url, brw=brw: self.updateLinkArea(url, brw))

    def goLink(self):
        u = QUrl(self.linkBar.text())
        if u.scheme() == "":
            u.setScheme("https")
        self.tab.currentWidget().setUrl(u)

    def updateLinkArea(self, u, brw=None):
        self.linkBar.setText(u.toString())

app = QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())