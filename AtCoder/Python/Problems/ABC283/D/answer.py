# import math
# from collections import defaultdict


# 文字列１個
# S = input()
# 数値 1個
# num = int(input())
# 数値２個
# N,M = map(int,input().split())
# 数値3個
# N,X,Y = map(int,input().split())

# リスト　文字列
strList = list(input())
# リスト　数値
# numList = list(map(int,input().split()))

pool = {}
open = []
close = []
openCnt = 0
ans = 'No'
for i in range(len(strList)):
    if strList[i] == '(':
        open.append(i)
        openCnt += 1
        ans = 'Yes'
    elif strList[i] == ')':
        close.append(i)
        openCnt -= 1
        openIndex = len(open) - len(close)
        J = open[openIndex]
        zan = strList[J:i]
        for key in pool:
            if key in zan:
                pool[key] -= 1
    elif openCnt > 0:
        if strList[i] in pool:
            if pool[strList[i]] == 0:
                pool[strList[i]] += 1
            elif pool[strList[i]] > 0:
                ans = 'No'
                break
        else:
            pool[strList[i]] = 1


print(ans)
