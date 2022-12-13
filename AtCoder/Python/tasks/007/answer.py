N,X,Y = map(int,input().split())

c = 0
for i in range(1,N+1):
    if i % Y == 0 or i % X == 0:
        c += 1
print(c)