from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *

import random

from numpy import fft


class sortArea: # 64열 시각화 막대 그래프 구역
    saved_list = []
    def __init__(self, sortArea: QGridLayout, Upper: QGridLayout, row, column):
        self.sortArea = sortArea # 기본 설정과
        self.sortArea.setSpacing(0) # 원래 쓰던 시각화 설정
        self.sortArea.setContentsMargins(0, 0, 0, 0)
        Upper.addLayout(self.sortArea, row, column) # 부모 설정까지

    def AreaUpdate(self, list):
        self.saved_list = list
        for i in reversed(range(self.sortArea.count())): # 그리드 청소용 코드 (퍼왔음)
            self.sortArea.itemAt(i).widget().deleteLater()

        for i in range(64): # 비우고 주어진 데이터로 새롭게 막대그래프 그려넣기
            label = QLabel()
            label.setStyleSheet("background-color: #ffffff; border: 1px solid #000000;")
            self.sortArea.addWidget(label, 63-list[i], i, list[i], 1)

    def AreaRecolor(self, index, color): # 시각화에서 비교중인 값 시각화용
        if color == 'red':
            hex='0000'
        else:
            hex='ffff'
        label = QLabel()
        label.setStyleSheet(f"background-color: #ff{hex}; border: 1px solid #000000;")
        self.sortArea.addWidget(label, 63-self.saved_list[index], index, self.saved_list[index], 1)


    def TestUI(self, num): # 임시용 땜빵라벨
        label = QLabel(f"Area {num}")
        color = f'{random.randrange(0, 256):02X}'+f'{random.randrange(0, 256):02X}'+f'{random.randrange(0, 256):02X}'
        label.setStyleSheet(f"background-color: #{color};")
        self.sortArea.addWidget(label)