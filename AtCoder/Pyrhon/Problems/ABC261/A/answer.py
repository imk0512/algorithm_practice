a,b,c,d = map(int,input().split())

if((c <= a and a <= d) and b <= d):
    result = b - a
elif((c <= a and a <= d) and b > d):
    result = d - a
elif((a <= c and c <= b) and d <= b):
    result = d - c
elif((a <= c and c <= b) and d > b):
    result = b - c
else:
    result = 0

if(result <= 0):
    print(0)
else:
    print(result)