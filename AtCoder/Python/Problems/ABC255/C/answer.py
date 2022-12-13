list = list(map(int,input().split()))

import math

def permutationWithRepetition(n, r):
    return int(pow(n, r))


def permutationWithRepetitionList(data, r):
    length = len(data)
    total = permutationWithRepetition(length, r)
    result = []
    for i in range(total):
        element = []
    for digit in reversed(range(r)):
        element.append(data[int(i / pow(length, digit)) % length])
        result.append(element)
    return result

val = permutationWithRepetition(0,3)

print(val)