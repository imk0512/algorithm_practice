import copy

# from collections import defaultdict


# 文字列１個
# N = input()
# 数値 1個
# num = int(input())
# 数値２個
N, P, Q, R, S = map(int, input().split())
AList = list(input().split())
BList = copy.deepcopy(AList)
BList[P - 1 : Q] = AList[R - 1 : S]
BList[R - 1 : S] = AList[P - 1 : Q]
print(*BList)
