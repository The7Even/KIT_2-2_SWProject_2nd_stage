# 멍청이 정렬 Prototype
# index 0 ~ 63
import random

sortList = [ ]
randomList = [ ]
completeList = [ ]
for i in range(64):
    randomList.append(i) # 랜덤 리스트 index 0~63 채워넣기
    completeList.append(i)

for i in range(64):
    tar = randomList[random.randint(0,len(randomList)-1)]
    sortList.append(tar)
    randomList.remove(tar) # 길이 64의 랜덤리스트 생성

resultList = sortList.copy()
# 예능용 알고리즘
while 1:
    if resultList == completeList: # 혹시라도 정렬이 완료될경우 탈출
        break

    tar1 = random.randint(0,63)
    tar2 = random.randint(0,63)

    randomList[tar1], randomList[tar2] = randomList[tar2], randomList[tar1] # 랜덤으로 둘이 바꿔버리기

print(sortList)
print(randomList)