from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtWidgets import *

import random
import sys

from AreaInit import sortArea
from SortAlgorithm import *

class mainwindow(QMainWindow):
    rndlist = []

    def __init__(self):
        super().__init__()

        for i in range(64):
            self.rndlist.append(i)

        # -----------------스레드 구역 (시각화 처리 )-----------------------
        self.insertThread = None

        self.ui_init()

    def createRndlist(self, a1:sortArea, a2:sortArea, a3:sortArea):
        self.rndlist = []
        randomList = []
        for i in range(64):
            randomList.append(i)  # 랜덤 리스트 index 0~63 채워넣기

        for i in range(64):
            tar = randomList[random.randint(0, len(randomList) - 1)]
            self.rndlist.append(tar)
            randomList.remove(tar)  # 길이 64의 랜덤리스트 생성

        print(self.rndlist)
        a1.AreaUpdate(self.rndlist)
        a2.AreaUpdate(self.rndlist)
        a3.AreaUpdate(self.rndlist)

    def InsertRun(self):
        if self.insertThread is not None and self.insertThread.isRunning():
            return

        self.insertThread = InsertSort(self.rndlist)
        self.insertThread.update_screen.connect(self.sortArea1.AreaUpdate)
        self.insertThread.pointRecolor.connect(self.sortArea1.AreaRecolor)

        self.insertThread.start()

    def ui_init(self): # 기초 UI 구성
        self.setFixedSize(1280, 720) # 가로 1280 - 세로 720의 16:9비
        self.setWindowTitle("Sort Algorithm Visualizer")

        BigLayout = QVBoxLayout() # 상단 : 작동 정보, 중단 : 정렬 시각화 구역, 하단 : 버튼모음
    # GridBox로 구상을 하는게 어떨지... GridBox로 64*64 크기쓰면 괜찮을 거 같은데..
        sortVisualCell = QGridLayout() # 3개 정렬 시각화 및 나머지 하나는 현재 작동 정보 작성

    # --------------상단 구역 ( 알고리즘 작동 정보 구역 )------------------
        infoLabel = QLabel("상단 구역용 임시 Label")
        infoLabel.setStyleSheet("background-color: #ff0000;")

        BigLayout.addWidget(infoLabel, 0)

    # -----------------중단 구역 ( 알고리즘 시각화 구역 )--------------------
        self.sortArea1 = sortArea(QHBoxLayout(), sortVisualCell, 0, 0) # 커스텀 클래스 기반 시각화 구역
        self.sortArea2 = sortArea(QHBoxLayout(), sortVisualCell,0, 1)
        self.sortArea3 = sortArea(QHBoxLayout(), sortVisualCell,1, 0)
        self.sortInfo = QVBoxLayout()

        sortVisualCell.addLayout(self.sortInfo, 1, 1)

        label4 = QLabel("Area 4")
        label4.setStyleSheet("background-color: #00ffff;")

        self.sortArea1.AreaUpdate(self.rndlist)
        self.sortArea2.AreaUpdate(self.rndlist)
        self.sortArea3.AreaUpdate(self.rndlist)
        self.sortInfo.addWidget(label4)

        BigLayout.addLayout(sortVisualCell, 1)

    # -----------------하단 구역 ( 기능 제어 구역 )--------------------
        underButtonBox = QHBoxLayout()

        area1SortButton = QPushButton("TEST1")
        area1SortButton.setStyleSheet("background-color: #aaaaff;")
        area1SortButton.clicked.connect(self.InsertRun)

        shuffleButton = QPushButton("Shuffle")
        shuffleButton.setStyleSheet("background-color: #aaaaff;")
        shuffleButton.clicked.connect(lambda: self.createRndlist(self.sortArea1, self.sortArea2, self.sortArea3))

        underButtonBox.addWidget(shuffleButton)
        underButtonBox.addWidget(area1SortButton)

        BigLayout.addLayout(underButtonBox,0)

    # ------------------마감 구역 ( 시각화 처리 )-----------------------
        widget = QWidget()
        widget.setLayout(BigLayout)
        self.setCentralWidget(widget)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = mainwindow()
    sys.exit(app.exec())