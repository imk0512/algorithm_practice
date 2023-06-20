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
    N = int(ip())
    line = lmv(int)
    d = {}
    for i in range(len(line)):
        d[i] = line[i]
    
    c = 0
    d2 = {}
    for k in dict(sorted(d.items(), key=lambda x:x[1])).keys():
        d2[k] = c
        c += 1
    
    print(*dict(sorted(d2.items())).values())
    pass
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------