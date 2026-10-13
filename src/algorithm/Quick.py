# 퀵 정렬 Prototype
# index 0 ~ 63 (N log_2 n시 384)
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
# 기본 알고리즘 구상..
# 우선 피벗값 지정하고 뭐시기 해야되는데..
# 일단 초기 피벗값잡고 반갈시키고 앞에 끝내고 뭐시기...
def quick(list):
    if len(list) <= 1: # 길이가 1 이하라면 이거는 이미 정렬이 끝남.
        return list

    pivot = list[0]
    other = list[1:]

    left = [x for x in list if x < pivot] # 피벗보다 작은 리스트
    right = [x for x in list if x > pivot] # 피벗보다 큰 리스트

    return quick(left) + [pivot] + quick(right) # 재귀함수 이용 퀵정렬 continue

resultList = quick(resultList)
print(sortList)
print(resultList)

''' 
이걸 시각화 어떻게 할 지 고민하는 공간

일단 지금 구현된 퀵정렬은 걍 간단하게 리스트에서 피벗보다 작은값, 큰값들 싹다 모아버리는 그런방식인데
전통적인 퀵정렬이랑은 완전히 다른 구조로 구성되어 있음..

만약에 이걸 좀 다르게 구성한다고 하면 색깔입혀주던지 뭐 그래야될거같은데..
아니면 이걸 좀 다르게 구성하던가..

아무튼 지금 이 상태로 프로젝트에 바로 넣는건 무리가 있어보임. 이걸 정석으로 구현하던지, 아니면 이대로 넣고 시각적으로 삐까뻔쩍하게 수정해주던지..
'''