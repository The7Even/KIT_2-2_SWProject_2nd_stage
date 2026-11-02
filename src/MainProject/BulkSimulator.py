import random, csv

from PyQt6.QtGui import QUndoCommand

# BulkSimulator
# 대용량 실행을 전제로 구성되는 파일
# 3가지 알고리즘을 시행횟수만큼 시행하고 그 결과를 csv로 출력
# 출력시킬 결과는 다음과 같음.
# 1. 평균 수행 시간 (총 수행 시간 / sim_time)
# 2. 평균 array_access, compare 수
# 3. 평균 순위 (3가지 알고리즘 상대 비교)
# 4. 수행 시간의 편차 (각 수행의 array_access와 compare의 합을 수행시간으로 가정)
# 그럼 이렇게 저장한다면?
# 회차 Insert_array Insert_comp Insert_Runtime Insert_Rank 이하 4가지 요소 전부 추가.
# 시행 횟수는 아래 변수에 값을 저장
sim_time = 10000

# 출력 파일은 여기에 디렉토리 지정 (.csv 출력)
sim_dir = 'C:\\Users\\USER\\Desktop\\KIT\\26-02 files\\SW프로젝트\\2nd stage\\Project'

QuickResult = [0,0,0]

def quick(list): # 시각화용 quick 구상
    if len(list) <= 1: return list

    pivot = list[0]
    other = list[1:] # 일단 여기까지는 똑같이 해도 상관없을거같은데..

    pointLow = 0
    pointHigh = len(other) -1 # 좌우포인터

    while 1:
        # 여기서 Low_High 두개 교차할때까지 Loop
        if other[pointLow] > pivot:
            other[pointLow], other[pointHigh] = other[pointHigh], other[pointLow]
            QuickResult[0] += 1
        else:
            pointLow += 1

        QuickResult[1] += 1
        if pointHigh < pointLow:
            break

        if other[pointHigh] < pivot:
            other[pointHigh], other[pointLow] = other[pointLow], other[pointHigh]
            QuickResult[0] += 1
        else:
            pointHigh -= 1

        QuickResult[1] += 1
        if pointHigh < pointLow:
            break

    left = other[:pointHigh+1]
    right = other[pointLow:]

    return quick(left) + [pivot] + quick(right)

resultList = [["Simulation Num",
               "Insert_Array", "Insert_Comp", "Insert_Runtick",
               "Bubble_Array", "Bubble_Comp", "Bubble_Runtick",
               "Quick_Array", "Quick_Comp", "Quick_Runtick",
               "Insert_Rank", "Bubble_Rank", "Quick_Rank"]]

temp_list = []
for i in range(64):
    temp_list.append(i)

for k in range(sim_time):
    beforelst = temp_list.copy()
    random.shuffle(beforelst) # 어???????????? 이게된다고??????

    tarlst = beforelst.copy()
    InsertResult = [0, 0]
    for i in range(64):
        num = tarlst[i]
        breakPos = 0

        for j in range(i):  # 0에서 시작하면 어떻게됨?
            # 가정 : i = 5라면 6번째 데이터 (List[5] 값을 정렬하기 위해 이동하는 상태. List[4] > List[0] 이동. j가 0 > 4로 이동하니까 4-0, 4-1...
            InsertResult[1] += 1 # 이게 어떻게 200대가 나오지??
            if num > tarlst[i - 1 - j]:
                breakPos = i - j  # 만약 4 > 0 이동중 [2]에서 발견했다면 j값은 아마 2일것임. 삽입위치는 [3]
                break

        tarlst.remove(num)
        tarlst.insert(breakPos, num)
        InsertResult[0] += 1 # 얘는 64가 정상인데...

    InsertResult.append(InsertResult[0]+InsertResult[1])

    tarlst = beforelst.copy()
    BubbleResult = [0, 0]
    for i in range(63):  # 일단 여기는 종료 지점을 [63]에서 [1]까지 줄여야하기 때문에.. 총 63회 반복해야 함.
        for j in range(63 - i):  # 여기는 [0]과 [1], [1]과 [2]... 해서 끝까지 가는 반복문
            BubbleResult[1] += 1
            if tarlst[j] > tarlst[j + 1]:
                BubbleResult[0] += 1
                tarlst[j], tarlst[j + 1] = tarlst[j + 1], tarlst[j]  # 와 이런식으로도 바꿀수가 있네

    BubbleResult.append(BubbleResult[0]+BubbleResult[1])
    tarlst = beforelst.copy()
    QuickResult = [0, 0, 0]

    tarlst = quick(tarlst)
    QuickResult[2] = QuickResult[0] + QuickResult[1]

    rank_ori = [InsertResult[2], BubbleResult[2], QuickResult[2]]
    rank_tar = sorted(rank_ori)
    rank = []

    for i in rank_ori:
        for j in range(3):
            if i == rank_tar[j]:
                rank.append(j+1)


    fin_lst = [k+1]
    for i in InsertResult:
        fin_lst.append(i)
    for i in BubbleResult:
        fin_lst.append(i)
    for i in QuickResult:
        fin_lst.append(i)
    for i in rank:
        fin_lst.append(i)

    resultList.append(fin_lst)

with open(sim_dir + '\\result.csv', 'w', newline='') as file:
    writer = csv.writer(file)

# 쭉 작성해서 출력하기.
    writer.writerows(resultList)