# 3つ以上の最小公倍数

import functools
import math

N = int(input())
nList = list(map(int, input().split()))


def my_lcm_base(x, y):
    return (x * y) // math.gcd(x, y)


def my_lcm(*integers):
    return functools.reduce(my_lcm_base, integers)


print(my_lcm(*nList))
