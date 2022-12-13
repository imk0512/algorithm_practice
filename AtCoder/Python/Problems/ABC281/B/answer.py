S = input()

s = S[0]
e = S[-1]

if not s.isnumeric() and not e.isnumeric():
    pre = S[1:]

    re = pre[:-1]
    if re.isnumeric():
        if int(re) >=100000 and int(re) <=999999 and len(re) ==6:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
else:
    print('No')