from collections import deque
n1,n2,m=map(int,input().split())
n=n1+n2
g=[[] for i in range(n)]

def bfs(s):
    dist=[-1]*n
    dist[s]=0
    q=deque([s])
    while q:
        now=q.popleft()
        for to in g[now]:
            if dist[to]==-1:
                dist[to]=dist[now]+1
                q.append(to)
    return max(dist)

for i in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    g[a].append(b)
    g[b].append(a)

print(bfs(0)+bfs(n-1)+1)