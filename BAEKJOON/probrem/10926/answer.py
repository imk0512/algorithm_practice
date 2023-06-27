import sys

# python3 answer.py < input.txt
# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))

n,m = mv(int)
print(n+m)
print(n-m)
print(n*m)
print(n//m)
print(n%m)