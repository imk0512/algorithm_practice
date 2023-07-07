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
    for _ in range(n):
        s = ip()
        chars = list(s)
        stack = []
        for str in chars:
            if str == "(":
                if len(stack) == 0:
                    stack.append(str)
                else:
                    bef = stack[-1]
                    if bef == "(":
                        stack.append(str)
                    else:
                        stack.append(str)
                        break
            else:
                if len(stack) == 0:
                    stack.append(str)
                    break
                else:
                    bef = stack[-1]
                    if bef == "(":
                        stack.pop(0)
                    else:
                        stack.append(str)
                        break
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------