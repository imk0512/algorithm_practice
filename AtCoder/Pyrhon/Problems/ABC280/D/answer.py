import math

N = int(input())

import functools
def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a%b)
def multiple(a, b):
    return a*b // euclid(a, b)

def lcm(nums):
        return functools.reduce(multiple, nums)


num = list(map(int, input().split()))
print(lcm(N))