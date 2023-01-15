# import math
# from collections import defaultdict

N = int(input())
S = input()

flg = False
ans = ''
for i in range(N):
    st = S[i]
    if st == '"':
        flg = not flg
    if flg:
        ans = ans + st
        continue
    else:
        if st == ',':
            ans = ans + '.'
        else:
            ans = ans + st

print(ans)