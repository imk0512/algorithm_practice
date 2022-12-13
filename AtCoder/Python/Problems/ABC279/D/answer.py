import math

A,B = map(int,input().split())
def solve (g,min):
    squareRoot = math.sqrt(g)
    return (1 * (min)) + ( A / squareRoot)

now = 0
last = 0
count = 1
min = 0
g = 1
min = 1
mid = (1 + A) / 2
max = A
while True:
    testA = solve(min,g)
    testB = solve(max,max / B)
    
    testB = solve(b)
    testC = solve(c)
    
    if min == 0:
        last = now
    g += 1
    min += B
    if now > last:
        print(last)
        break
    last = now

