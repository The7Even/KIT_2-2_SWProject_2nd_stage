import time

from PyQt6.QtCore import QThread, pyqtSignal, pyqtSlot

from AreaInit import sortArea

class InsertSort(QThread):
    update_screen = pyqtSignal(list) # 스레드에서 UI 갱신 요청용.
    pointRecolor = pyqtSignal(int, str) # 이렇게 하면 되려나?

    def __init__(self, data_list):
        super().__init__()
        self.data_list = list(data_list)

    def run(self):
        lst = self.data_list

        # 색 변경 기준 (빨강, 이 외 전부 하양)
        # 1. 현재 num값
        # 2. num값과 비교되고 있는 값
        for i in range(64):
            num = lst[i]
            breakPos = 0
            self.pointRecolor.emit(i, 'red') # 기준 1에 따라 색칠됨.

            for j in range(i): #여기가 기준 2인데 # j값은 0에서 출발함. 지켜보는값은 0이 아니라 i-1-j부터
                self.pointRecolor.emit(i-1-j, 'red') # 그러니 일단 그자식부터 색칠
                if j != 0: # j가 0이면 i 자신이기에 조건문
                    self.pointRecolor.emit(i-j, 'white')
                if num > lst[i-1-j]: # 만약 이 반복문을 빠져나간다면 지켜보고 있는 두 값이 변화함. i-1-j는 그대로겠고, 그리고 i-j값(breakPos)도 빨개짐.
                    breakPos = i-j
                    self.pointRecolor.emit(i, 'white') # 그럼 원래위치는 하얗게 바꾸고
                    break
                self.update_screen.emit(list(lst))
                time.sleep(0.01)

            lst.remove(num)
            lst.insert(breakPos, num)
            self.pointRecolor.emit(breakPos, 'red') # 여기가 빨개지겠고
            self.update_screen.emit(list(lst))
            time.sleep(0.01)
            self.pointRecolor.emit(breakPos, 'white') # 다시 하얘지기
            self.pointRecolor.emit(breakPos-1, 'white') # 너도 하얘지면 초기값

class BubbleSort(QThread):
    update_screen = pyqtSignal(list)  # 이것들은 공통이라 사실..
    pointRecolor = pyqtSignal(int, str)

    def __init__(self, data_list):
        super().__init__()
        self.data_list = list(data_list)

    def run(self):
        lst = self.data_list

        for i in range(63):  # 일단 여기는 종료 지점을 [63]에서 [1]까지 줄여야하기 때문에.. 총 63회 반복해야 함.
            for j in range(63 - i):  # 여기는 [0]과 [1], [1]과 [2]... 해서 끝까지 가는 반복문
                if j != 0:
                    self.pointRecolor.emit(j-1, 'white')
                self.pointRecolor.emit(j, 'red')
                self.pointRecolor.emit(j+1, 'red')
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]  # 와 이런식으로도 바꿀수가 있네
                    self.update_screen.emit(list(lst))
                time.sleep(0.01)

            self.pointRecolor.emit(j, 'white')
            self.pointRecolor.emit(j+1, 'white')

class QuickSort(QThread):
    update_range_screen = pyqtSignal(list, int)
    pointRecolor = pyqtSignal(int, str)

    def __init__(self, data_list):
        super().__init__()
        self.data_list = list(data_list)

    def quickReturn(self, list_data, pos):  # 재귀함수
        tarlist = list_data.copy()
        if len(list_data) <= 1: return list_data

        pivot = tarlist[0]
        self.pointRecolor.emit(pos, 'blue') # 일단 피벗값 시각화처리

        pointLow = 1
        pointHigh = len(tarlist) - 1  # 좌우포인터
        self.pointRecolor.emit(pos+pointLow, 'green')
        self.pointRecolor.emit(pos+pointHigh, 'red')

        while 1: # Low를 초록, High를 빨강으로 표시
            # 여기서 Low_High 두개 교차할때까지 Loop
            if tarlist[pointLow] > pivot:
                tarlist[pointLow], tarlist[pointHigh] = tarlist[pointHigh], tarlist[pointLow]
                self.update_range_screen.emit(list(tarlist), pos)
            else:
                self.pointRecolor.emit(pos+pointLow, 'white')
                pointLow += 1
                if pointLow <= pointHigh:
                    self.pointRecolor.emit(pos+pointLow, 'green')

            time.sleep(0.01)

            if pointHigh < pointLow:
                self.pointRecolor.emit(pos + pointLow, 'white')
                self.pointRecolor.emit(pos + pointHigh, 'white')
                break

            if tarlist[pointHigh] < pivot:
                tarlist[pointLow], tarlist[pointHigh] = tarlist[pointHigh], tarlist[pointLow]
                self.update_range_screen.emit(list(tarlist), pos)
            else:
                self.pointRecolor.emit(pos+pointHigh, 'white')
                pointHigh -= 1
                if pointLow <= pointHigh:
                    self.pointRecolor.emit(pos+pointHigh, 'red')

            time.sleep(0.01)

            if pointHigh < pointLow:
                self.pointRecolor.emit(pos+pointLow, 'white')
                self.pointRecolor.emit(pos+pointHigh, 'white')
                self.pointRecolor.emit(pos, 'white')
                break

        time.sleep(0.01) # LR 구분 완료 후 pivot값 색상해제 및 전체 색상 해제
        tarlist[0], tarlist[pointHigh] = tarlist[pointHigh], tarlist[0]
        left = tarlist[:pointHigh]
        right = tarlist[pointHigh+1:]
        self.pointRecolor.emit(pos, 'white')
        self.update_range_screen.emit(list(tarlist), pos)

        return self.quickReturn(left, pos) + [pivot] + self.quickReturn(right, pos + pointHigh+1)

    def run(self):
        lst = self.data_list

        self.quickReturn(lst,0)