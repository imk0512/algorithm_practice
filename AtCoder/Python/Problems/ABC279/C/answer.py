H, W = input().split()

hight = int(H)

slint = []
tlist = []
for n in range(hight):
    slint.append(input())
for m in range(hight):
    tlist.append(input())

j = True
for n in range(hight):
    s = slint[n]
    t = tlist[n]
    scount = s.count('#')
    tcount = t.count('#')

    if(scount != tcount):
        j = False

if j:
    print('Yes')
else:
    print('No')
