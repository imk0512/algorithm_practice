# import math
# from collections import defaultdict


# 文字列１個
# N = input()
# 数値 1個
# num = int(input())
# 数値２個
N,M = map(int,input().split())
# 数値3個
# N,X,Y = map(int,input().split())

# リスト　文字列
#  strList = list(map(input().split()))
# リスト　数値
# numList = list(map(int,input().split()))

score = []
for _ in range(N):
    l = list(input())
    score.append(l)

count = 0
for i in range(N):
    for j in range(N):
        if i == j or i < j:
            continue
        else:
            iscore = score[i]
            jsocre = score[j]
            round = 0
            for v in range(M):
                if iscore[v] == 'o' or jsocre[v] == 'o':
                    round += 1

            if round == M:
                count += 1

print(count)