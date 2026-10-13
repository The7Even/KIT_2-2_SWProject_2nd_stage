from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *

import sys

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_init()

    def ui_init(self): # 기초 UI 구성
        self.setFixedSize(1280, 720) # 가로 1280 - 세로 720의 16:9비
        self.setWindowTitle("Sort Algorithm Visualizer")

        BigLayout = QVBoxLayout() # 상단 : 작동 정보, 중단 : 정렬 시각화 구역, 하단 : 버튼모음
    # GridBox로 구상을 하는게 어떨지... GridBox로 64*64 크기쓰면 괜찮을 거 같은데..
        sortVisualCell = QGridLayout() # 3개 정렬 시각화 및 나머지 하나는 현재 작동 정보 작성

    # 상단 구역 ( 알고리즘 작동 정보 구역 )
        infoLabel = QLabel("상단 구역용 임시 Label")
        infoLabel.setStyleSheet("background-color: #ff0000;")

        BigLayout.addWidget(infoLabel, 0)

    # 중단 구역 ( 알고리즘 시각화 구역 )
        sortArea1 = QGridLayout()
        sortArea2 = QGridLayout()
        sortArea3 = QGridLayout()
        sortInfo = QVBoxLayout()

        sortVisualCell.addLayout(sortArea1, 0, 0)
        sortVisualCell.addLayout(sortArea2, 0, 1)
        sortVisualCell.addLayout(sortArea3, 1, 0)
        sortVisualCell.addLayout(sortInfo, 1, 1)

        label1 = QLabel("Area 1")
        label2 = QLabel("Area 2")
        label3 = QLabel("Area 3")
        label4 = QLabel("Area 4")
        label1.setStyleSheet("background-color: #00ff00;")
        label2.setStyleSheet("background-color: #0000ff;")
        label3.setStyleSheet("background-color: #ff0000;")
        label4.setStyleSheet("background-color: #00ffff;")

        sortArea1.addWidget(label1)
        sortArea2.addWidget(label2)
        sortArea3.addWidget(label3)
        sortInfo.addWidget(label4)

        BigLayout.addLayout(sortVisualCell, 1)

    # 하단 구역 ( 기능 제어 구역 )
        underButtonBox = QHBoxLayout()
        testButton = QPushButton("TEST")
        testButton.setStyleSheet("background-color: #ffff00;")
        underButtonBox.addWidget(testButton)

        BigLayout.addLayout(underButtonBox,0)

    # 마감 구역 ( 시각화 처리 )
        widget = QWidget()
        widget.setLayout(BigLayout)
        self.setCentralWidget(widget)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = mainwindow()
    sys.exit(app.exec())