import copy
def solve(list):
    c = 1
    result = 0
    for item in list:
        result += item * c
        c +=1
    return result

N,M = map(int,input().split())
line = list(map(int,input().split()))

case = []

for i in range(M + 1):

    front = M - i
    back = i
    case.append([front,back])

resultList = []
print(case)
for c in case:
    pre = copy.copy(line)
    if c[0] > 0:
        del pre[:c[0]]
    if c[1] > 0:
        s = 0 - c[1]
        del pre[s:]
    resultList.append(solve(pre))

resultList.sort(reverse=True)

print(resultList)
print(resultList[0])