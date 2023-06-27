import sys

# python3 answer.py < input.txt
# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def dfs(graph, start, visited):
    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited
# -------------------------------


# Please write the code below ---
def main():
    n = int(ip())
    m = int(ip())
    graph = {}
    for i in range(n):
        graph[i+1] = []
    for _ in range(m):
        v = lmv(int)
        graph[v[0]].append(v[1])
        graph[v[1]].append(v[0])
    visited = set()
    c= dfs(graph,1,visited)
    print(len(c)-1)
    pass
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------