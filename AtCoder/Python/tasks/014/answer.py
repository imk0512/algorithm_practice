number = int(input())

# 素因数分解　列挙
"""nを素因数分解"""
"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-(n**0.5) // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


ansList = factorization(number)
## [[2, 3], [3, 1]]
##  24 = 2^3 * 3^1

## [2,2,2,3]
flat = []
for line in ansList:
    for _ in range(line[1]):
        flat.append(line[0])
print(*flat)
