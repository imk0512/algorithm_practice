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
    x,y = mv(int)
    box = [[1,2,3],[4,5,6],[7,8,9]]

    line = []
    for l in box:
        if x in l:
            line = l
    
    if y in line:
        if (x + 1) == y:
            print('Yes')
        elif (x -1) == y:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------