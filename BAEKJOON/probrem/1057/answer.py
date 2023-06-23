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
    r,k,i = mv(int)

    if r % 2 != 0:
        r += 1
    cnt = 1
    isMatch = False
    while True:
        l = list(range(1,int(r)+1))
        if r == 1:
            cnt = -1
            break
        for j in range(0,r,2):
            f = l[j]
            if j + 1 >= len(l):
                break
            s = l[j + 1]
            if f == k and s == i:
                isMatch = True
                break
            if f == i and s == k:
                isMatch = True
                break
        if isMatch:
            break
        else:
            if i % 2 != 0:
                i += 1
            if k % 2 != 0:
                k += 1
            if r % 2 != 0:
                r += 1
            r = int(r / 2)
            k = int(k / 2)
            i = int(i / 2)
            cnt += 1
    print(cnt)
    pass
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------