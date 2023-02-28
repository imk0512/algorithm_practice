N = int(input())
XList = list(map(int, input().split()))

XList.sort()

for _ in range(N):
    XList.pop(0)
    XList.pop(-1)

total = 0
for i in XList:
    total = total + i
score = total / len(XList)
print(score)
