import sys

# python3 answer.py < input.txt
# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def min_operations(N):
    dp = [0]*(N+1)

    for i in range(2, N+1):
        # 1を引く操作を考慮
        dp[i] = dp[i-1] + 1

        # 2で割る操作を考慮
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)

        # 3で割る操作を考慮
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)
    
    return dp[N]
# -------------------------------


# Please write the code below ---
def main():
	N = int(input())
	print(min_operations(N))
  
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------