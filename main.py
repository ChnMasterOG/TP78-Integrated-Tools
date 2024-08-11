
import ui_main
import ui_tp78foc
import ui_via
import ui_news

import os
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtWidgets import QFrame, QGraphicsScene
from PyQt5.QtGui import QPixmap

import requests
import re
import json

software_version = "V1.0.0"
download_url = ""
version_news = ""
information_news = ""
image_list = []
cur_news_image_idx = 0

def check_new_release():
    global download_url
    global version_news
    try:
        response = requests.get("https://api.github.com/repos/ChnMasterOG/TP78-Integrated-Tools/releases").json()
        for release in response:
            if release["tag_name"] >= software_version:
                print("find new software version: %s" % (release["tag_name"]))
                download_url = release["assets"][0]["browser_download_url"]
                print("get download url: %s" % (download_url))
                version_news = release["body"]
                print("release note: %s" % (version_news))
                version_news = "Relase note: " + version_news + "\n\n"
                return True
    except:
        print("Network error!")
    return False

def check_new_images():
    global image_list
    global pixmap
    try:
        response = requests.get("https://github.com/ChnMasterOG/TP78-Integrated-Tools/tree/main/buffer")
        urls = re.findall("\w+\.png", response.text)
        new_urls = list(set(urls))
        local_flist = os.listdir("./buffer")
        for u in new_urls:
            prefix_u = u.split("_")[0]
            for f in local_flist:
                if prefix_u == f[:len(prefix_u)] and f[-4:] == ".png" and u > f:
                    print("download: " + u)
                    image_resp = requests.get("https://raw.githubusercontent.com/ChnMasterOG/TP78-Integrated-Tools/main/res/" + u)
                    with open(p, "wb") as f:
                        f.write(image_resp.content)
                    os.remove(f)
    except:
        print("Network error!")
    image_list = []
    local_flist = os.listdir("./buffer/")
    l = len(local_flist)
    for f_idx in range(l):
        if local_flist[f_idx][-4:] == ".png":
            image_list.append(local_flist[f_idx])
    newsWin.scene.clear()
    pixmap = QPixmap(os.path.join("./buffer", image_list[0]))
    newsWin.scene.addPixmap(pixmap)

class NewsWindow(QMainWindow,ui_news.Ui_Form): 
    def __init__(self,parent =None):
        super(NewsWindow,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.graphicsView.setFrameShape(QFrame.NoFrame)
        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.graphicsView.show()
        self.next_button.clicked.connect(self.next_button_on_click)
        self.close_button.clicked.connect(self.close_button_on_click)
 
    def next_button_on_click(self):
        global cur_news_image_idx
        cur_news_image_idx += 1
        if cur_news_image_idx >= len(image_list):
            cur_news_image_idx = 0
        self.scene.clear()
        pixmap = QPixmap(os.path.join("./buffer", image_list[cur_news_image_idx]))
        self.scene.addPixmap(pixmap)

    def close_button_on_click(self):
        self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    if not(os.path.exists("buffer")):
        os.mkdir("buffer")
    newsWin = NewsWindow()
    check_new_images()
    if check_new_release() == False:
        newsWin.download_button.hide()
    newsWin.note_label.setText(version_news + information_news)
    newsWin.show()
    sys.exit(app.exec_())



