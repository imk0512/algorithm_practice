a,b = map(int,input().split())

c = 0
for i in range(1, a+1):
    for l in range(1, a+1):
        if(i + l <= b):
            c += 1
        
print(c)