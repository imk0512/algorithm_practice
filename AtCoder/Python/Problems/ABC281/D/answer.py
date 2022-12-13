from itertools import combinations
N,K,D =  map(int,input().split())
a = list(map(int,input().split()))

com = list(map(sum,combinations(a,K)))
com.reverse()


re = [n for n in com if n % D == 0]

if len(re) > 0:
    print(max(re))
else:
    print(-1)