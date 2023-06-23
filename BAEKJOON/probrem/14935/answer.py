import sys

# python3 answer.py < input.txt
# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------

def solve(n:str) :
    res =  int(n[0]) * len(n)
    return str(res)

# -------------------------------


# Please write the code below ---
def main():
    n = ip()
    bef = ''
    while True:
        n = solve(n)
        # if len(n) == 1:
        #     print('NFA')
        #     break
        if bef == n:
            print('FA')
            break
        bef = n
    pass
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------