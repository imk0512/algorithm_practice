N,T =  map(int,input().split())
list = list(map(int,input().split()))

re = 0
index = 0
if T < sum(list):
    for i in range(N):
        T = T - list[i]
        if T <= 0:
            re = list[i] + T
            index = i
            break
elif T > sum(list):
    round = T // sum(list)
    T = T - round * sum(list)
    for i in range(N):
        T = T - list[i]
        if T <= 0:
            re = list[i] + T
            index = i
            break


str = "{} {}".format(index + 1, re)
print(str)