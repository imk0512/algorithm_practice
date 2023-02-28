# import math
# from collections import defaultdict


# 文字列１個
# N = input()
# 数値 1個
# num = int(input())
# 数値２個
a, b = map(int, input().split())


if b == a * 2:
    print("Yes")
elif b == a * 2 + 1:
    print("Yes")
else:
    print("No")
