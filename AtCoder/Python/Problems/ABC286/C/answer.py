# import math
# from collections import defaultdict


# 文字列１個
# N = input()
# 数値 1個
# num = int(input())
# 数値２個
# N, M = map(int, input().split())
# 数値3個
# N,X,Y = map(int,input().split())

# リスト　文字列
strList = list(input())
# リスト　数値
# numList = list(map(int,input().split()))


import string

alphabets = string.ascii_uppercase

ans = 0


for num in range(len(strList)):
    ans *= 26
    n = alphabets.index(strList[num]) + 1
    ans += n

print(ans)
