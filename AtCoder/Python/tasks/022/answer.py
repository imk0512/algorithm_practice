N = int(input())
A = list(map(int, input().split()))
target = 100000
cards = [0] * target
for a in A:
    cards[a] += 1
ans = 0
for i in range(1, target // 2):
    ans += cards[i] * cards[target - i]

print(cards)
