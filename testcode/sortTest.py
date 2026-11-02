lst = [323, 255, 645]

sortlst = sorted(lst)
print(sortlst)

rank = []
for i in sortlst:
    for j in range(3):
        if i == lst[j]:
            rank.append(j+1)

print(rank)