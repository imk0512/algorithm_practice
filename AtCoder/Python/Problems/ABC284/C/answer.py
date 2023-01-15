N, M = map(int, input().split())


ans = N
d = []
for i in range(M):
    d.append(set(list(map(int, input().split()))))

ansList = []
for obj1 in d:
    for obj2 in d:
        if obj1 & obj2:
            ansList.append(obj1.union(obj2))

print(ansList)
