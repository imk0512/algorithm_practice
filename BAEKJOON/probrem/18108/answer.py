import sys

# python3 answer.py < input.txt
# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------
base = [1, 1, 2, 2, 2, 8]
l = lmv(int)

ans = []
for i in range(len(base)):
    ans.append(base[i] - l[i])
        

print(*ans)