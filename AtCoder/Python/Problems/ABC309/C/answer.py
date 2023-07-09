import sys

# python3 answer.py < input.txt
# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def mvlmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------

# -------------------------------


# Please write the code below ---
def main():
    N,K = mv(int)
    d = {}
    for _ in range(N):
        p,x = mv(int)
        if d.get(p) is not None:
            d[p] = d[p] + x
        else:
            d[p] = x
    t = sum(d.values())
    if t <= K:
        print(1)
        exit(0)
    sorted_dict = dict(sorted(d.items(), key=lambda x: x[0]))

    for k,v in sorted_dict.items():
        t -= v
        if t <= K:
            print(k +1)
            break
    pass
# -------------------------------


# Inore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------