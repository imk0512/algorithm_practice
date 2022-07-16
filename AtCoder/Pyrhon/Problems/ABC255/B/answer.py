X,A,D,N = map(int,input().split())

list =[]
for i in range(1,N):
    an = A + (i -1) * D
    list.append(an)

print(list)