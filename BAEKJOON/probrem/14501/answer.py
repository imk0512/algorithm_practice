import sys
import math
# python3 answer.py < input.txt
# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def max_profit(N, consult):
    dp = [0] * (N + 2)

    for i in range(N, 0, -1):
        if i + consult[i][0] <= N + 1:
            dp[i] = max(consult[i][1] + dp[i + consult[i][0]], dp[i + 1])
        else:
            dp[i] = dp[i + 1]

    return dp[1]
# -------------------------------


# Please write the code below ---
def main():
    n = int(ip())
    works = [[0,0]]

    for _ in range(n):
        t,p = mv(int)
        works.append([t,p])
    ans =max_profit(n,works)
    print(ans)

# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------