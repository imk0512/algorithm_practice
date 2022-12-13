N,M = map(int,input().split())
hitList = list(map(int,input().split()))
bonusLists = {}
for _ in range(M):
    C,Y = map(int,input().split())
    bonusLists[C] = Y



print(bonusLists)