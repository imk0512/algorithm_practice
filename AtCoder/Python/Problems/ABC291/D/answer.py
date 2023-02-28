import itertools

num = int(input())

cards = {}
for i in range(1, num + 1):
    cards[i] = list(map(int, input().split()))


def solve(conb, obj):
    pre = 0
    for k, v in obj.items():
        if k in conb:
            if pre == obj[k][1]:
                return False
        else:
            if pre == obj[k][0]:
                return False
        pre = v
    return True


cnt = 0
for n in range(1, len(cards) + 1):
    for conb in itertools.combinations(cards, n):
        if solve(conb, cards):
            cnt = cnt + 1
print(cnt)
