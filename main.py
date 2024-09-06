
import tp78_config_tool.main
import ui_main
import ui_tp78foc
import ui_via
import ui_news

import os
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QFrame, QGraphicsScene, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QThread, pyqtSignal, QObject
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

import requests
import re
import time
import _thread
import webbrowser
import random
import platform

import tp78_foc_firmware_download as foc_download_lib
import tp78_config_tool

random.seed()
system_platform = platform.system()
if system_platform == 'Linux':
    cur_file_path = os.path.dirname(os.path.realpath(sys.argv[0]))
else:
    cur_file_path = os.getcwd()
software_version = "V1.0.0"
download_url = ""
version_news = ""
information_news = ""
image_list = []
cur_news_image_idx = 0

information_news_list = [
    "● 无私奉献不是天方夜谭，有时候，我们也可以做到。",
    "● 如果你没有把握做到，最好就不要承诺。",
    "● 不要害怕产生BUG，因为BUG永远解不完。",
    "● 要么做第一个，要么做最好的一个。",
    "● 设计是一个发现问题、而不是发现解决方案的过程。",
    "● 想知道TP78v3，那是个秘密，不能告诉你。",
    "● 永不放弃有两个原则，第一个原则是永不放弃，第二个原则就是：当你想放弃时回头看第一个原则。",
    "● 不是井里没有水,而是挖的不够深。不是成功来得慢,而是努力的不够狠。",
    "● 你看工具里为啥有灰的按钮，因为有人在偷懒没做。",
    "● 如果你有更好的建议，请在QQ群里告诉我们。",
]

def get_cur_path_with(str):
    return os.path.join(cur_file_path, str)

def check_new_release():
    global download_url
    global version_news
    try:
        response = requests.get("https://gitee.com/api/v5/repos/ChnMasterOG/TP78-Integrated-Tools/releases").json()
        for release in response:
            if release["tag_name"] >= software_version:
                print("find new software version: %s" % (release["tag_name"]))
                download_url = release["assets"][0]["browser_download_url"]
                print("get download url: %s" % (download_url))
                version_news = release["body"]
                print("release note: %s" % (version_news))
                version_news = "新版本更新内容: " + version_news + "\n"
                return True
    except:
        print("Network error!")
    return False

def check_new_images():
    global image_list
    global pixmap
    try:
        response = requests.get("https://gitee.com/ChnMasterOG/TP78-Integrated-Tools/tree/main/buffer")
        urls = re.findall("TP78\w+\.png", response.text)
        new_urls = list(set(urls))
        local_flist = os.listdir(get_cur_path_with("./buffer"))
        for u in new_urls:
            prefix_u = u.split("_")[1]
            download_new_image_flag = True
            for f in local_flist:
                if f[:4] != "TP78":
                    continue
                prefix_local = f.split("_")[1]
                if prefix_u == prefix_local[:len(prefix_u)] and f[-4:] == ".png":   # 已存在图片
                    if u <= f:  # 图片版本是新的
                        download_new_image_flag = False
                    else:   # 删除旧的
                        os.remove(os.path.join(get_cur_path_with("./buffer"), f))
                    break
            if download_new_image_flag == True:
                print("download: " + u)
                image_resp = requests.get("https://gitee.com/ChnMasterOG/TP78-Integrated-Tools/raw/main/buffer/" + u)
                with open(os.path.join(get_cur_path_with("./buffer"), u), "wb") as f:
                    f.write(image_resp.content)
    except:
        print("Network error!")
    image_list = []
    local_flist = os.listdir(get_cur_path_with("./buffer"))
    l = len(local_flist)
    for f_idx in range(l):
        if local_flist[f_idx][-4:] == ".png":
            image_list.append(local_flist[f_idx])

def check_new_via_json():
    global image_list
    global pixmap
    try:
        response = requests.get("https://gitee.com/ChnMasterOG/TP78-Integrated-Tools/tree/main/buffer")
        urls = re.findall("\w+\.json", response.text)
        new_urls = list(set(urls))
        for u in new_urls:
            if u.find("layout") != -1:
                print("download: " + u)
                image_resp = requests.get("https://gitee.com/ChnMasterOG/TP78-Integrated-Tools/raw/main/buffer/" + u)
                with open(os.path.join(get_cur_path_with("./buffer"), u), "wb") as f:
                    f.write(image_resp.content)
    except:
        print("Network error!")

class tp78_foc_update_progress_Worker(QObject):
    progress_signal = pyqtSignal(int)
    error_signal = pyqtSignal(str)

    def run(self):
        temp = 0
        while True:
            if temp != foc_download_lib.progress_percent:
                temp = foc_download_lib.progress_percent
                self.progress_signal.emit(temp)
            if temp == 100 or foc_download_lib.error_log != "":
                if foc_download_lib.error_log != "":
                    self.error_signal.emit(foc_download_lib.error_log)
                    foc_download_lib.error_log = ""
                temp = 0
                foc_download_lib.progress_percent = 0
                tp78focWin.Button_selectfirmware.setEnabled(True)
                tp78focWin.Button_update.setEnabled(True)
            time.sleep(0.1)

class tp78_foc_firmware_download_Worker(QObject):
    def __init__(self):
        super(tp78_foc_firmware_download_Worker,self).__init__()
        self.firmware_path = ""
        self.begin_flag = False

    def run(self):
        while True:
            if self.begin_flag == True:
                self.begin_flag = False
                foc_download_lib.firmware_download_progress(self.firmware_path)
    
    def set_firmware_path(self, path):
        self.firmware_path = path
        print(self.firmware_path)
    
    def begin(self, flag):
        self.begin_flag = flag

class tp78_news_check_Worker(QObject):
    new_release = pyqtSignal(bool)
    note_news = pyqtSignal(str)

    def __init__(self):
        super().__init__()
 
    def run(self):
        check_new_images()
        new_release_flag = check_new_release()
        check_new_via_json()
        random_number = random.randrange(0, len(information_news_list))
        information_news = information_news_list[random_number]
        news = version_news + information_news
        self.note_news.emit(news)
        self.new_release.emit(new_release_flag)

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
        self.download_button.clicked.connect(self.download_button_on_click)
 
    def next_button_on_click(self):
        global cur_news_image_idx
        cur_news_image_idx += 1
        if cur_news_image_idx >= len(image_list):
            cur_news_image_idx = 0
        self.scene.clear()
        pixmap = QPixmap(os.path.join(get_cur_path_with("./buffer"), image_list[cur_news_image_idx]))
        self.scene.addPixmap(pixmap)

    def close_button_on_click(self):
        self.hide()

    def download_button_on_click(self):
        global download_url
        try:
            webbrowser.open(download_url)
        except:
            pass

class MainWindow(QMainWindow,ui_main.Ui_Form): 
    def __init__(self,parent =None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.Button_TP78.clicked.connect(self.tp78_button_on_click)
        self.Button_TP78MINI.setEnabled(False)
        self.Button_TP78FOC.clicked.connect(self.tp78foc_button_on_click)
        self.Button_VIA.clicked.connect(self.via_show)
        self.Button_MagnetAxis.setEnabled(False)
        # TP78 news checker
        self.news_checker_thread = QThread()
        self.tp78_news_check_worker = tp78_news_check_Worker()
        self.tp78_news_check_worker.moveToThread(self.news_checker_thread)
        self.tp78_news_check_worker.note_news.connect(self.tp78news_show)
        self.tp78_news_check_worker.new_release.connect(self.tp78news_release_set)
        self.news_checker_thread.started.connect(self.tp78_news_check_worker.run)
        #self.news_checker_thread.finished.connect(self.news_checker_thread.deleteLater)
        self.news_checker_thread.start()

    def tp78_button_on_click(self):
        _thread.start_new_thread(tp78_config_tool.main.tp78_config_tool_main, ())

    def tp78foc_button_on_click(self):
        tp78focWin.show()
    
    def tp78news_show(self, news):
        pixmap = QPixmap(os.path.join(get_cur_path_with("./buffer"), image_list[0]))
        newsWin.scene.clear()
        newsWin.scene.addPixmap(pixmap)
        newsWin.show()
        newsWin.note_label.setText(news)

    def tp78news_release_set(self, is_enable):
        if is_enable == False:
            newsWin.download_button.hide()

    def via_show(self):
        url = 'https://usevia.app/'
        try:
            webbrowser.open(url)
        except:
            pass

class TP78focWindow(QMainWindow,ui_tp78foc.Ui_Form): 
    firmware_path_signal = pyqtSignal(str)
    begin_download_signal = pyqtSignal(bool)

    def __init__(self,parent =None):
        super(TP78focWindow,self).__init__(parent)
        self.setupUi(self)
        self.progressBar.setValue(0)
        self.setFixedSize(self.width(), self.height())
        self.Button_selectfirmware.clicked.connect(self.select_firmware)
        self.Button_update.clicked.connect(self.download_firmware)
        self.selected_firmware_path_label.setWordWrap(True)
        self.firmware_path = ""
        #*** thread ***#
        self.tp78_foc_update_progress_worker = tp78_foc_update_progress_Worker()
        self.tp78_foc_update_progress_thread = QThread()
        self.tp78_foc_update_progress_worker.moveToThread(self.tp78_foc_update_progress_thread)
        self.tp78_foc_update_progress_worker.progress_signal.connect(self.update_progress)
        self.tp78_foc_update_progress_worker.error_signal.connect(self.show_error_dialog)
        self.tp78_foc_update_progress_thread.started.connect(self.tp78_foc_update_progress_worker.run)
        self.tp78_foc_update_progress_thread.finished.connect(self.tp78_foc_update_progress_thread.deleteLater)
        self.tp78_foc_update_progress_thread.start()
        # self.tp78_foc_firmware_download_worker = tp78_foc_firmware_download_Worker()
        # self.tp78_foc_firmware_download_thread = QThread()
        # self.tp78_foc_firmware_download_worker.moveToThread(self.tp78_foc_firmware_download_thread)
        # self.firmware_path_signal.connect(self.tp78_foc_firmware_download_worker.set_firmware_path)
        # self.begin_download_signal.connect(self.tp78_foc_firmware_download_worker.begin)
        # self.tp78_foc_firmware_download_thread.started.connect(self.tp78_foc_firmware_download_worker.run)
        # self.tp78_foc_firmware_download_thread.start()

    def select_firmware(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getOpenFileName(self, 
                                                  "Open File", 
                                                  "", 
                                                  "All Files (*);;BIN Files (*.bin)", 
                                                  options=options)
        self.selected_firmware_path_label.setText("固件路径：" + fileName)
        self.firmware_path = fileName

    def download_firmware(self):
        self.Button_selectfirmware.setEnabled(False)
        self.Button_update.setEnabled(False)
        # self.firmware_path_signal.emit(self.firmware_path)
        # self.begin_download_signal.emit(True)
        _thread.start_new_thread(foc_download_lib.firmware_download_progress, (self.firmware_path, ))

    def update_progress(self, value):
        self.progressBar.setValue(value)

    def show_error_dialog(self, err):
        QMessageBox.critical(self, "Error", err)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    if not(os.path.exists("buffer")):
        os.mkdir("buffer")
    newsWin = NewsWindow()
    mainWin = MainWindow()
    tp78focWin = TP78focWindow()
    mainWin.show()
    sys.exit(app.exec_())



