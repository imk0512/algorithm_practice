from collections import defaultdict

N,M = map(int,input().split())

dict = defaultdict(set)
# G = [[0 for i in range(N)] for _ in range(N)]

# # count = [0 for i in range(N)]
for _ in range(M):
    u,v = map(int,input().split())
    dict[u].add(v)
    dict[v].add(u)

color = [0 for i in range(N+1)]
print(dict)