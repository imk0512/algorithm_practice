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
    if n == 1:
        print('1/1')
    else:
        total = 1
        cnt = 1
        while True:
            if total < n :
                total = total + (cnt + 1)
                cnt += 1
            else:
                break
        if cnt % 2 == 0:
            idx = total - n
            y = cnt - idx
            x = 1 + idx
            print(str(y)+'/'+str(x))
        else:
            idx = total - n
            x = cnt - idx
            y = 1 + idx
            print(str(y)+'/'+str(x))
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------