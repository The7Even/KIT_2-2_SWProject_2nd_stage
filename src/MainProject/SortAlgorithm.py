import time

from PyQt6.QtCore import QThread, pyqtSignal, pyqtSlot

from AreaInit import sortArea

class InsertSort(QThread):
    update_screen = pyqtSignal(list) # 스레드에서 UI 갱신 요청용. 이후 빨갛게 바꾸는것도 추가 예정
    pointRecolor = pyqtSignal(int, str) # 이렇게 하면 되려나?

    def __init__(self, data_list):
        super().__init__()
        self.data_list = list(data_list)
        self.is_running = True

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


def insertSort(Area:sortArea, list):
    Area.AreaUpdate(list) # 초기값 세팅

    for i in range(64):
        num = list[i]
        breakPos = 0

        for j in range(i): # 0에서 시작하면 어떻게됨?
            # 가정 : i = 5라면 6번째 데이터 (List[5] 값을 정렬하기 위해 이동하는 상태. List[4] > List[0] 이동. j가 0 > 4로 이동하니까 4-0, 4-1...
            if num > list[i-1-j]:
                breakPos = i-j # 만약 4 > 0 이동중 [2]에서 발견했다면 j값은 아마 2일것임. 삽입위치는 [3]
                break

        list.remove(num)
        list.insert(breakPos, num)
        Area.AreaUpdate(list)

