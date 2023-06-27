import sys

# python3 answer.py < input.txt
# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def tilingRectangle(n):
    # 動的計画法による方法の数の計算
    dp = [0] * (n + 1)

    # ベースケースの設定
    dp[1] = 1
    dp[2] = 2

    # 方法の数の計算
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007
    # nサイズの長方形を埋める方法の数を返す
    return dp[n]
# -------------------------------


# Please write the code below ---
def main():
    n = int(input())
    result = tilingRectangle(n)
    print(result)
    pass
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------