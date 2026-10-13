# 삽입 정렬 Prototype
# index 0 ~ 63 (N^2시 4096)
import random

sortList = [ ]
randomList = [ ]
for i in range(64):
    randomList.append(i) # 랜덤 리스트 index 0~63 채워넣기

for i in range(64):
    tar = randomList[random.randint(0,len(randomList)-1)]
    sortList.append(tar)
    randomList.remove(tar) # 길이 64의 랜덤리스트 생성

resultList = sortList.copy()
# N에서 출발, N-1에서 0으로 이동하면서 작은 값을 찾을때까지 검색
for i in range(64):
    num = resultList[i]
    breakPos = 0

    for j in range(i): # 0에서 시작하면 어떻게됨?
        # 가정 : i = 5라면 6번째 데이터 (List[5] 값을 정렬하기 위해 이동하는 상태. List[4] > List[0] 이동. j가 0 > 4로 이동하니까 4-0, 4-1...
        if num > resultList[i-1-j]:
            breakPos = i-j # 만약 4 > 0 이동중 [2]에서 발견했다면 j값은 아마 2일것임. 삽입위치는 [3]
            break

    resultList.remove(num)
    resultList.insert(breakPos, num)

print(sortList)
print(resultList)