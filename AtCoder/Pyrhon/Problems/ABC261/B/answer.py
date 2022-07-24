from pickle import TRUE


N = int(input())

tbl = [list(input()) for i in range(N)]

check = True
for i in range(N):
    listA = tbl[i]
    if(check == False):
        break
    for j in range(N):
        if(i == j):
            continue

        listB = tbl[j]

        if(listA[j] == 'D' and listB[i] != 'D'):
            print('incorrect')
            check = False
            break
        elif(listA[j] == 'W' and listB[i] != 'L'):
            print('incorrect')
            check = False
            break
        elif(listA[j] == 'L' and listB[i] != 'W'):
            print('incorrect')
            check = False
            break

if(check):
    print('correct')

