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
def sieve_of_eratosthenes(n):
    prime = [True for i in range(n+1)]
    prime[0] = False
    prime[1] = False

    sqrt_n = math.isqrt(n)
    for i in range(2, sqrt_n + 1):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False

    return prime
# -------------------------------


# Please write the code below ---
def main():
    m, n = mv(int)
    prime = sieve_of_eratosthenes(n)
    for i in range(m, n + 1): 
        if prime[i]:
            print(i)
    pass
    pass
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------