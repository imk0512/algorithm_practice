# 数値 1個
N = int(input())

# リスト　文字列
strList = list(input())
pointList = [[0, 0] for i in range(N + 1)]


for i in range(N):
    ope = strList[i]
    if ope == "R":
        pre = pointList[i]
        pointList[i + 1] = [pre[0] + 1, pre[1]]
    if ope == "L":
        pre = pointList[i]
        pointList[i + 1] = [pre[0] - 1, pre[1]]
    if ope == "U":
        pre = pointList[i]
        pointList[i + 1] = [pre[0], pre[1] + 1]
    if ope == "D":
        pre = pointList[i]
        pointList[i + 1] = [pre[0], pre[1] - 1]

dupl = list(map(list, set(map(tuple, pointList))))

if len(dupl) != len(pointList):
    print("Yes")
else:
    print("No")
