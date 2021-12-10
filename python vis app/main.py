import sys
import os
import PySide6
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QMainWindow, QApplication
from ui_mainwindow import Ui_MainWindow as MainUI
from PySide6.QtWebEngineWidgets import QWebEngineView

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = MainUI()
        self.ui.setupUi(self)

        path = os.path.dirname(os.path.abspath(__file__))

        self.webView = QWebEngineView()

        self.ui.verticalLayout.addWidget(self.webView)
        
        self.webView.load(QUrl.fromLocalFile(path+"\\arc_layer.html"))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())