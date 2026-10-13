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
                time.sleep(0.01)

            self.pointRecolor.emit(j, 'white')
            self.pointRecolor.emit(j+1, 'white')
