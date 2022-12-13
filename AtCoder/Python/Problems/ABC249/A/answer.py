a, b, c, d, e, f, x = map(int, input().split())

def solve(time,speed,rate, x):
    q = x // (time + rate)
    r = x % (time + rate)
    print(q)
    print(x // (time + rate))
    return (q * time + min(time,r)) * speed

lengthT = solve(a,b,c,x)
lengthA = solve(d,e,f,x)


if lengthT > lengthA:
    result = 'Takahashi'
elif lengthT < lengthA:
    result = 'Aoki'
elif lengthT == lengthA:
    result = 'Draw'
# print(result)
