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
#  strList = list(map(input().split()))
# リスト　数値
# numList = list(map(int,input().split()))


num = int(input())
list = []
for _ in range(num):
    list.append(input())


list = reversed(list)
for str in list:
    print(str)
