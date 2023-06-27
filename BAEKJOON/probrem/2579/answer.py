import sys

# python3 answer.py < input.txt
# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def solve(n, points):
    if n == 1:
        return points[0]
    dp = [0] * n
    dp[0] = points[0]
    dp[1] = max(points[0] + points[1], points[1])

    for i in range(2,n):
        dp[i] = max(dp[i - 3] + points[i-1] + points[i],dp[i - 2] + points[i])
    return dp[-1]
# -------------------------------


# Please write the code below ---
def main():
    n = int(input())
    stairs = [int(input()) for _ in range(n)]
    print(solve(n, stairs))
    pass
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------