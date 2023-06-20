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
    N = ip()
    line = lmv(int)
    ans = [i + 1 for i in len(line)]
    print(ans)
    for i in len(line):
        line
    pass
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------