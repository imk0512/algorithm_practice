# import math
# from collections import defaultdict


# 文字列１個
N = input()
list = ['00', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]

count = 0
f = False
for _ in range(len(N)):
    f = False
    for s in list:
        if not f:
            if N.startswith(s):
                if s == '00':
                    N = N[2:]
                    count += 1
                    f = True
                else:
                    N = N[1:]
                    count += 1
                    f = True
print(count)
