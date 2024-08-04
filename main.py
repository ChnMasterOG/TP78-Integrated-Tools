
import ui_main
import ui_tp78foc
import ui_via
import ui_news

import os
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication

import requests
import json

software_version = "V1.0.0"
download_url = ""
version_news = ""

def check_new_release():
    global download_url
    response = requests.get("https://api.github.com/repos/ChnMasterOG/TP78-Integrated-Tools/releases").json()
    for release in response:
        if release["tag_name"] >= software_version:
            print("find new software version: %s" % (release["tag_name"]))
            download_url = release["assets"][0]["browser_download_url"]
            print("get download url: %s" % (download_url))
            return True
    return False

class NewsWindow(QMainWindow,ui_news.Ui_Form): 
    def __init__(self,parent =None):
        super(NewsWindow,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    if not(os.path.exists("buffer")):
        os.mkdir("buffer")
    newsWin = NewsWindow()
    if check_new_release() == False:
        newsWin.download_button.hide()
    newsWin.show()
    sys.exit(app.exec_())    



