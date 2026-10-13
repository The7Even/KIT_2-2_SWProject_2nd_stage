# 버블 정렬 Prototype
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
# 기본 알고리즘
# 사실상 리스트 -1 위치부터 정렬이 되는 리버스 삽입정렬?
for i in range(63): # 일단 여기는 종료 지점을 [63]에서 [1]까지 줄여야하기 때문에.. 총 63회 반복해야 함.
    for j in range(63-i): # 여기는 [0]과 [1], [1]과 [2]... 해서 끝까지 가는 반복문
        if resultList[j] > resultList[j+1]:
            resultList[j], resultList[j+1] = resultList[j+1], resultList[j] # 와 이런식으로도 바꿀수가 있네

print(sortList)
print(resultList)

