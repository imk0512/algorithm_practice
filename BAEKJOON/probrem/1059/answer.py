import sys

def ip(): return sys.stdin.readline().strip()
def lmv(type): return list(map(type, sys.stdin.readline().strip().split()))

def main():
    L = int(ip())
    S = lmv(int)
    N = int(ip())
    S.sort()

    S = [0] + S + [1001]
    good_intervals = 0

    for i in range(1, len(S)):
        if S[i-1] < N < S[i]:
            left = N - S[i-1]
            right = S[i] - N
            good_intervals = (left * right) - 1
            break

    print(good_intervals)

if __name__ == "__main__":
    main()