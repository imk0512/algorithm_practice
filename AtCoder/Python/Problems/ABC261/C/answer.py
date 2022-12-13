N = int(input())

strList = [input() for i in range(N)]

strsMap = set(strList)

contMap = {}
for key in strsMap:
    contMap[key] = 0

for item in strList:
    cnt = contMap[item]

    if(cnt == 0):
        print(item)
    else:
        print(item + '('+str(cnt)+')')

    contMap[item] = cnt+1