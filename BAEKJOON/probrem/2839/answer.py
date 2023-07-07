import sys

# python3 answer.py < input.txt
# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def count_bags(n):
    # dp[i]: iキログラムの砂糖を作るための最小袋数
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(3, n + 1):
        dp[i] = min(dp[i], dp[i - 3] + 1)

    for i in range(5, n + 1):
        dp[i] = min(dp[i], dp[i - 5] + 1)

    if dp[n] == float('inf'):
        return -1
    else:
        return dp[n]
# -------------------------------


# Please write the code below ---
def main():
    n = int(input())

    result = count_bags(n)
    print(result)
        
    pass
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------