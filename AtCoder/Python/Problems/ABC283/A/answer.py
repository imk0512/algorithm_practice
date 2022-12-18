import string
list = list(string.ascii_lowercase)
ans = ''
N = int(input())
for s in range(N) :
    ans = ans + list[s].upper()
print(ans)