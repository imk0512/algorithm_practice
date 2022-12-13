str = input()
strs = list(str)
for s in strs:
    if(str.count(s) == 1):
        print(s)
        break
    if (str.count(s) == 3):
        print(-1)
        break
