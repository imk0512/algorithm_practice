import sys

# python3 answer.py < input.txt
# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------

# -------------------------------


# Please write the code below ---
def main():
    n = int(ip())
    ans = []
    for _ in range(n):
        c = int(ip())
        ans.append(c)
    ans.sort()
    for p in ans:
        print(p)
    pass

# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------