x,y = map(int,input().split())

c = 0
for _ in range(x):
    s = input()
    c += s.count('#')

print(c)