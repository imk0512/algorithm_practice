## 3つ以上の最大公約数

# ## python 3.9以降
# import math

# N = int(input())
# numList = list(map(int, input().split()))
# n = math.gcd(*numList)
# print(n)

## python 3.8以前

import functools
import math

N = int(input())
numList = list(map(int, input().split()))


def my_gcd(*integers):
    return functools.reduce(math.gcd, integers)


print(my_gcd(*numList))
