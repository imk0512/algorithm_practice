import sys

# python3 answer.py < input.txt
# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def solve(list,N):
    ans = 999999
    for brand in list:
            pack = brand[0]
            gen = brand[1]
            if pack < gen * N:
                if ans > pack:
                    ans = pack
            else:
                if ans > gen * N:
                    ans = gen * N
    return ans
# -------------------------------


# Please write the code below ---
def main():
    N,M = mv(int)
    brands = [lmv(int) for _ in range(M)]

    ans = 0
    if N <= 6 :
        ans = solve(brands,N)
    else:
        fullCase = []
        for brand in brands:
            pack = brand[0]
            gen = brand[1]
            fullCase.append(pack)
            fullCase.append(gen * 6)
        fullCase.sort()
        remaining = N % 6 
        ans = (fullCase[0] * (N//6)) + solve(brands,remaining)
    print(ans)

    pass
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------