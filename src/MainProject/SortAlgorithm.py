import time

from PyQt6.QtCore import QThread, pyqtSignal, pyqtSlot

from AreaInit import sortArea

class InsertSort(QThread):
    update_screen = pyqtSignal(list)

    def __init__(self, data_list):
        super().__init__()
        self.data_list = list(data_list)
        self.is_running = True

    def run(self):
        lst = self.data_list

        for i in range(64):
            num = lst[i]
            breakPos = 0

            for j in range(i):
                if num > lst[i-1-j]:
                    breakPos = i-j
                    break

            lst.remove(num)
            lst.insert(breakPos, num)
            self.update_screen.emit(list(lst))
            time.sleep(0.1)

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

