import math

n, r = map(int, input().split())
## 階乗の計算関数 nCr
## 公式
## nPr = n! / (n-r)!
## nCr = nPr / r! = n! / (n - r)! r!
rn = math.factorial(r)  ## 階乗関数　factorial
nn = math.factorial(n)
ans = nn // (rn * math.factorial((n - r)))
print(ans)
