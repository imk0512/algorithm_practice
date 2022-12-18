# import math
# from collections import defaultdict


# 文字列１個
# N = input()
# 数値 1個
# num = int(input())
# 数値２個
# N,S = map(int,input().split())
# 数値3個
X,Y,N = map(int,input().split())

# リスト　文字列
# strList = list(map(input().split()))
# リスト　数値
# numList = list(map(int,input().split()))

if X * 3 > Y:
    print((N // 3) * Y + (N % 3) * X)
else:
    print(X * N)