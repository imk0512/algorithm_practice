# import math
# from collections import defaultdict


# 文字列１個
# N = input()
# 数値 1個
# num = int(input())
# 数値２個
# N,S = map(int,input().split())
# 数値3個
# N,X,Y = map(int,input().split())

# リスト　文字列
# strList = list(map(input().split()))
# リスト　数値
numList = list(map(int, input().split()))

data_set = set(numList)

if len(data_set) == 2:
    a = data_set.pop()
    b = data_set.pop()
    if (numList.count(a) == 2 or numList.count(a) == 3) and (numList.count(b) == 2 or numList.count(b) == 3):
        print("Yes")
    else :
        print("No")
else:
    print("No")
