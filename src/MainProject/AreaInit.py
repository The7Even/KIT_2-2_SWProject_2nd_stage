from PyQt6.QtCore import Qt, QObject, pyqtSlot, pyqtSignal
from PyQt6.QtWidgets import *

import random

class sortArea(QObject): # 64열 시각화 막대 그래프 구역
    # 윈도우 기본 크기 720중에서 640 할당. 뭐 부족하면 윈도우 좀 더 잡아당기지.
    # 결국 720 > 810 확장 진행
    # 640 할당인데 2행이므로 한칸당 320 배정됨. 길이값 1당 5픽셀
    def __init__(self, sortArea: QHBoxLayout, Upper: QGridLayout, row, column):
        super().__init__()
        self.saved_list = []
        self.sortArea = sortArea # 기본 설정과
        self.sortArea.setSpacing(0) # 원래 쓰던 시각화 설정
        self.sortArea.setContentsMargins(0, 0, 0, 0)
        Upper.addLayout(self.sortArea, row, column) # 부모 설정까지

        self.bars = []
        self.sortArea.setAlignment(Qt.AlignmentFlag.AlignBottom) # 길이 조정해도 밑으로 쏠리게

        for i in range(64):
            label = QLabel()
            label.setStyleSheet("background-color: #ffffff; border: 1px solid #000000;")
            self.bars.append(label)
            sortArea.addWidget(label, 0, Qt.AlignmentFlag.AlignBottom)

    @pyqtSlot(list)
    def AreaUpdate(self, lst):
        self.saved_list = lst.copy()
        for i in range(64):
            barLength = lst[i]+1

            self.bars[i].setFixedHeight(barLength*5)

    @pyqtSlot(list, int)
    def AreaRangeUpdate(self, list, pos): # pos값을 3으로 주면 index가 3인 4번째 값부터 수정이 들어갈 예정.
        for i in range(len(list)):
            self.saved_list[pos+i] = list[i] # 리스트 일부 범위 수정
            barLength = list[i]+1

            self.bars[pos+i].setFixedHeight(barLength*5)

    @pyqtSlot(int, str)
    def AreaRecolor(self, index, color): # 시각화에서 비교중인 값 시각화용
        if index >= 0 and index < 64:
            if color == 'red':
                hex='ff0000'
            elif color == 'blue':
                hex='0000ff'
            elif color == 'green':
                hex='00ff00'
            else:
                hex='ffffff'
            self.bars[index].setStyleSheet(f"background-color: #{hex}; border: 1px solid #000000;")

class ResultLabel(QLabel):
    def __init__(self, sort_type: str, delay:int):
        super().__init__()
        self.compare = 0
        self.array = 0
        self.sortType = sort_type
        self.timeDiff = ''
        self.delay = delay

        self.labelUpdate()

    def reset(self):
        self.compare = 0
        self.array = 0

    @pyqtSlot(int)
    def compareEvent(self, num: int):
        self.compare += num
        self.labelUpdate()

    @pyqtSlot()
    def arrayEvent(self):
        self.array += 1
        self.labelUpdate()

    def labelUpdate(self):
        if self.sortType == 'Insertion':
            self.timeDiff = 'O(n²)'
        elif self.sortType == 'Bubble':
            self.timeDiff = 'O(n²)'
        elif self.sortType == 'Quick':
            self.timeDiff = 'O(n log n)'

        self.setText(f"{self.sortType} Sort - {self.timeDiff}\ncomparison - {self.compare} / array access - {self.array}\ndelay - {self.delay}ms")