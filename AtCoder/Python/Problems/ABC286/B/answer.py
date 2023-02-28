N = int(input())
S = input()


def solve(S: str, i: int):
    l = 0
    for k in range(len(S)):
        if i + k >= len(S):
            break
        if S[k] != S[k + i]:
            l += 1
        else:
            break
    return l


for i in range(1, N):
    print(solve(S, i))
