import sys

# python3 answer.py < input.txt
# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def solve(n,m):
    maxSuq = 0
    if n > m:
        maxSuq = n - m
    elif m > n:
        maxSuq = m - n
    else:
        maxSuq = m
    pass
# -------------------------------


# Please write the code below ---
def main():
    n,m = mv(int)

    suq = [lmv(int) for _ in range(n)]

    pass
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------