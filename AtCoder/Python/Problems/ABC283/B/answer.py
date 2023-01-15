
N = int(input())
AList = list(map(int,input().split()))
Q = int(input())

for i in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 2:
        print(AList[query[1] - 1])
    else:
        AList[query[1] -1] = query[2]
