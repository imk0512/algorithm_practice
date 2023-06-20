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
    N = int(ip())
    A = lmv(int)
    B = lmv(int)

    A.sort()
    B.sort(reverse=True)
    ans = 0
    for i in range(N):
        ans = ans + (A[i] * B[i])
    print(ans)
    pass
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------