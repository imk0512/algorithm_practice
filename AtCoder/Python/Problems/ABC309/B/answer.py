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
    box = [list(ip()) for _ in range(n)]
    ans = []
    for i in range(n):
        ans.append([0]*n)
    for i in range(n):
        for j in range(n):
            if i == 0:
                if j == 0:
                    ans[i][j] = box[i+1][j]
                elif j < n:
                    ans[i][j] = box[i][j -1]
                # elif j == n -1:
                #     ans[i+1][j]= box[i][j]
            if i > 0 and i < n - 1:
                if j == 0:
                    ans[i][j] = box[i +1][j]
                elif j == (n-1):
                    ans[i][j] = box[i-1][j]
                else:
                    ans[i][j] = box[i][j]
            if i == n-1:
                if j == n-1:
                    ans[i][j] = box[i-1][j]
                elif j < n-1:
                    ans[i][j] = box[i][j+1]

                
        pass
    for a in ans:
        print(''.join(a))
    pass
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------