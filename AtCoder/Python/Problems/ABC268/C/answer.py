N, Q = input().split()


# list = [[0 for i in range(int(N))] for j in range(int(N))]
# print(list)
HashMap = {}

for _ in range(int(Q)):
    T,A,B = map(int,input().split())
    if not A in HashMap:
        HashMap[A] = {B : 0}
    if not B in HashMap:
        HashMap[B] = {A : 0}
    if T == 1:
        HashMap[A][B] = 1
    if T == 2:
        HashMap[A][B] = 0
    if T == 3:
        AType = False
        BType = False
        if A in HashMap:
            if B in HashMap[A]:
                if HashMap[A][B] == 1:
                    AType = True


        if B in HashMap:
            if A in HashMap[B]:
                if HashMap[B][A] == 1:
                    BType = True
        if BType and AType:
            print('Yes')
        else:
            print('No')