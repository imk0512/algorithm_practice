# import math
# from collections import defaultdict


# 文字列１個
# N = input()
# 数値 1個
num = int(input())
# 数値２個
# N,S = map(int,input().split())
# 数値3個
# N,X,Y = map(int,input().split())

# リスト　文字列
# strList = list(map(input().split()))
# リスト　数値
# numList = list(map(int,input().split()))


if num % 4 == 2:
    print(num)
elif num % 4 == 1:
    print(num + 1)
elif num % 4 == 3:
    print(num + 3)
elif num % 4 == 0:
    print(num + 2)
