H, M = input().split()

Hlist = list(H)
Mlist = list(M)
A = '0'
B = '0'
C = '0'
D = '0'


if len(Hlist) > 1:
    A = Hlist[0]
    B = Hlist[1]
else:
    B = Hlist[0]

if len(Mlist) > 1:
    C = Mlist[0]
    D = Mlist[1]
else:
    D = Mlist[0]

TopH = 0
underM = 0
while True :
    TopH = int(A + C)
    underM = int(B + D)

    if TopH >= 0 and TopH <= 23 and underM >= 0 and underM <= 59:
        print(A+B+' ' + C+D)
        break

    if int(D) <= 8:
        D = str(int(D) + 1)
    else :
        D = '0'
        if int(C) <= 4:
            C = str(int(C) + 1)
        else:
            C = '0'
            if int(B) <= 8 and int(A) <= 1:
                B = str(int(B) + 1)
            elif int(B) <= 2 and int(A) == 2:
                B = str(int(B) + 1)
            elif int(B) == 9 and int(A) == 1:
                B = '0'
                A = '2'
            else :
                B = '0'
                A = '0'

