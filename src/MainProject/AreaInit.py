from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *

import random

class sortArea: # 64열 시각화 막대 그래프 구역
    # 윈도우 기본 크기 720중에서 640 할당. 뭐 부족하면 윈도우 좀 더 잡아당기지.
    # 640 할당인데 2행이므로 한칸당 320 배정됨. 길이값 1당 5픽셀
    saved_list = []
    def __init__(self, sortArea: QHBoxLayout, Upper: QGridLayout, row, column):
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

    def AreaUpdate(self, list):
        self.saved_list = list
        for i in range(64):
            barLength = list[i]+1

            self.bars[i].setFixedHeight(barLength*5)

    def AreaRecolor(self, index, color): # 시각화에서 비교중인 값 시각화용
        if color == 'red':
            hex='0000'
        else:
            hex='ffff'
        self.bars[index].setStyleSheet(f"background-color: #ff{hex}; border: 1px solid #000000;")


    def TestUI(self, num): # 임시용 땜빵라벨
        label = QLabel(f"Area {num}")
        color = f'{random.randrange(0, 256):02X}'+f'{random.randrange(0, 256):02X}'+f'{random.randrange(0, 256):02X}'
        label.setStyleSheet(f"background-color: #{color};")
        self.sortArea.addWidget(label)