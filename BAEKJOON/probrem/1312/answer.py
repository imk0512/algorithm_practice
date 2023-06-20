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
def find_decimal_digit(A, B, N):
    for _ in range(N):
        A = (A % B) * 10
    return A // B
# -------------------------------


# Please write the code below ---
def main():
    A, B, N = map(int, input().split())
    print(find_decimal_digit(A, B, N))
    pass
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------