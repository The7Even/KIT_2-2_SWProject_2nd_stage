from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *

import random

class sortArea: # 그리드 레이아웃과 데이터를 받아와야함.
    def __init__(self, sortArea: QGridLayout, Upper: QGridLayout, row, column):
        self.sortArea = sortArea
        self.sortArea.setSpacing(0)
        self.sortArea.setContentsMargins(0, 0, 0, 0)
        Upper.addLayout(self.sortArea, row, column)

    def AreaUpdate(self, list):
        for i in reversed(range(self.sortArea.count())): # 그리드 청소용 코드 (퍼왔음)
            self.sortArea.itemAt(i).widget().deleteLater()

        for i in range(64):
            label = QLabel()
            label.setStyleSheet("background-color: #ffffff; border: 1px solid #000000;")
            self.sortArea.addWidget(label, 63-list[i], i, list[i], 1)

    def TestUI(self, num):
        label = QLabel(f"Area {num}")
        color = f'{random.randrange(0, 256):02X}'+f'{random.randrange(0, 256):02X}'+f'{random.randrange(0, 256):02X}'
        label.setStyleSheet(f"background-color: #{color};")
        self.sortArea.addWidget(label)