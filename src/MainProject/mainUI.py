from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtWidgets import *

import random
import sys

from AreaInit import sortArea, ResultLabel
from SortAlgorithm import *

class mainwindow(QMainWindow):
    rndlist = []

    def __init__(self):
        super().__init__()

        for i in range(64):
            self.rndlist.append(i)

        # -----------------스레드 구역 (시각화 처리 )-----------------------
        self.insertThread = None
        self.bubbleThread = None
        self.quickThread = None

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

        a1.AreaUpdate(self.rndlist)
        a2.AreaUpdate(self.rndlist)
        a3.AreaUpdate(self.rndlist)

    def InsertRun(self):
        if self.insertThread is not None and self.insertThread.isRunning():
            return

        self.result1.reset()
        self.insertThread = InsertSort(self.rndlist)
        self.insertThread.update_screen.connect(self.sortArea1.AreaUpdate)
        self.insertThread.pointRecolor.connect(self.sortArea1.AreaRecolor)
        self.insertThread.update_status_compare.connect(self.result1.compareEvent)
        self.insertThread.update_status_array.connect(self.result1.arrayEvent)

        self.insertThread.start()

    def BubbleRun(self):
        if self.bubbleThread is not None and self.bubbleThread.isRunning():
            return

        self.result2.reset()
        self.bubbleThread = BubbleSort(self.rndlist)
        self.bubbleThread.update_screen.connect(self.sortArea2.AreaUpdate)
        self.bubbleThread.pointRecolor.connect(self.sortArea2.AreaRecolor)
        self.bubbleThread.update_status_compare.connect(self.result2.compareEvent)
        self.bubbleThread.update_status_array.connect(self.result2.arrayEvent)

        self.bubbleThread.start()

    def QuickRun(self):
        if self.quickThread is not None and self.quickThread.isRunning():
            return

        self.result3.reset()
        self.quickThread = QuickSort(self.rndlist)
        self.quickThread.update_range_screen.connect(self.sortArea3.AreaRangeUpdate)
        self.quickThread.pointRecolor.connect(self.sortArea3.AreaRecolor)
        self.quickThread.update_status_array.connect(self.result3.arrayEvent)
        self.quickThread.update_status_compare.connect(self.result3.compareEvent)

        self.quickThread.start()

    def RunAll(self):
        self.InsertRun()
        self.BubbleRun()
        self.QuickRun()

    def ui_init(self): # 기초 UI 구성
        self.setFixedSize(1280, 720) # 가로 1280 - 세로 720의 16:9비
        self.setWindowTitle("Sort Algorithm Visualizer")

        BigLayout = QVBoxLayout() # 상단 : 작동 정보, 중단 : 정렬 시각화 구역, 하단 : 버튼모음
    # GridBox로 구상을 하는게 어떨지... GridBox로 64*64 크기쓰면 괜찮을 거 같은데..
        sortVisualCell = QGridLayout() # 3개 정렬 시각화 및 나머지 하나는 현재 작동 정보 작성

    # --------------상단 구역 ( 알고리즘 작동 정보 구역 )------------------
        infoLabel = QLabel("왼쪽 위부터 각 삽입 정렬, 버블 정렬, 퀵정렬입니다. (각 step별 delay = 10ms)")
        infoLabel.setStyleSheet("background-color: #ffffff;")

        BigLayout.addWidget(infoLabel, 0)

    # -----------------중단 구역 ( 알고리즘 시각화 구역 )--------------------
        self.sortArea1 = sortArea(QHBoxLayout(), sortVisualCell, 0, 0) # 커스텀 클래스 기반 시각화 구역
        self.sortArea2 = sortArea(QHBoxLayout(), sortVisualCell,0, 1)
        self.sortArea3 = sortArea(QHBoxLayout(), sortVisualCell,1, 0)
        self.resultArea = QGridLayout() # 결과 정리용 Grid - 비교연산, 교환연산 진행량 표시, 남는 한칸은 진행 시간 표시.
        sortVisualCell.addLayout(self.resultArea, 1, 1)

    # 구역 4를 다시 한번 또 Grid로 줘서 위치별 정보를 주고 우측 하단은 진행 시간이라던가 그런 정보를 보여줘도 괜찮을지도?
        self.result1 = ResultLabel("Insertion")
        self.result2 = ResultLabel("Bubble")
        self.result3 = ResultLabel("Quick")
        self.timeResult = QLabel("Time Spent - \nInsertion - 0000ms\nBubble - 0000ms\nQuick - 0000ms")

        self.resultArea.addWidget(self.result1, 0,0)
        self.resultArea.addWidget(self.result2, 0,1)
        self.resultArea.addWidget(self.result3, 1,0)
        self.resultArea.addWidget(self.timeResult, 1,1)

        self.sortArea1.AreaUpdate(self.rndlist)
        self.sortArea2.AreaUpdate(self.rndlist)
        self.sortArea3.AreaUpdate(self.rndlist)

        BigLayout.addLayout(sortVisualCell, 1)

    # -----------------하단 구역 ( 기능 제어 구역 )--------------------
        underButtonBox = QHBoxLayout()

        area1SortButton = QPushButton("Area 1 - Insert")
        area1SortButton.setStyleSheet("background-color: #aaaaff;")
        area1SortButton.clicked.connect(self.InsertRun)

        area2SortButton = QPushButton("Area 2 - Bubble")
        area2SortButton.setStyleSheet("background-color: #aaaaff;")
        area2SortButton.clicked.connect(self.BubbleRun)

        area3SortButton = QPushButton("Area 3 - Quick")
        area3SortButton.setStyleSheet("background-color: #aaaaff;")
        area3SortButton.clicked.connect(self.QuickRun)

        allSortButton = QPushButton("Sort All")
        allSortButton.setStyleSheet("background-color: #aaaaff;")
        allSortButton.clicked.connect(self.RunAll)

        shuffleButton = QPushButton("Shuffle")
        shuffleButton.setStyleSheet("background-color: #aaaaff;")
        shuffleButton.clicked.connect(lambda: self.createRndlist(self.sortArea1, self.sortArea2, self.sortArea3))

        underButtonBox.addWidget(shuffleButton)
        underButtonBox.addWidget(area1SortButton)
        underButtonBox.addWidget(area2SortButton)
        underButtonBox.addWidget(area3SortButton)
        underButtonBox.addWidget(allSortButton)

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