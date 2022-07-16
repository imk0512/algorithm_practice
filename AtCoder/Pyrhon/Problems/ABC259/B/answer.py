N = int(input())
lists = list(map(int,input().split()))

runners = [0] * N

P = 0
cnt = 0
for i in lists:
    cnt += 1
    for j in range(cnt):
        runners[j] += i


for item in runners:
    if item >= 4:
        P += 1

print(P)