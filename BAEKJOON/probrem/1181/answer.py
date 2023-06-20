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
    x = int(ip())
    words = [ip() for _ in range(x)]
    s = sorted(set(words))
    s.sort(key=lambda i : len(i))
    for a in s:
        print(a)    
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------