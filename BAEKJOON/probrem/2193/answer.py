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
    dp = [0 for i in range(n + 10)]
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    if n  > 2 :
        for i in range(2,n + 1):
            dp[i] = dp[i-1] + dp[i-2]
    print(dp[n])

# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------