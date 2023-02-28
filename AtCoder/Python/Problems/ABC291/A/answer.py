S = input()

c = 0
for s in S:
    c = c + 1
    if s.isupper():
        print(c)
        break
