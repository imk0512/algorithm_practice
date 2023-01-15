N = int(input())


ansList = []
for _ in range(N):
    count = 0
    c = int(input())
    numList = list(map(int, input().split()))

    for o in numList:
        if o % 2 != 0:
            count += 1

    ansList.append(count)

for a in ansList:
    print(a)
