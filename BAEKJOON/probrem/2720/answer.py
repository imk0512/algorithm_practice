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
    t = int(ip())
    q,d,n,p = [25,10,5,1]
    for _ in range(t):
        m = int(ip())
        ans = [0,0,0,0]
        if (m // q) >= 1:
            ans[0] = m//q
            m -= (m//q) * q
        if (m // d) >= 1:
            ans[1] = m//d
            m -= (m//d) * d
        if (m // n) >= 1:
            ans[2] = m//n
            m -= (m//n) * n
        if (m // p) >= 1:
            ans[3] = m//p
            m -= m//p
        print(*ans)

    pass
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------