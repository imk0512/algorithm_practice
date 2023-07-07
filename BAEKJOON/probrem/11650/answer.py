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
    coordinates = [lmv(int) for _ in range(n)]
    coordinates.sort(key=lambda x: (x[0], x[1]))
    for s in coordinates:
        print(*s)

# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------