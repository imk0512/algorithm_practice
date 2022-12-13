pins = list(input())

if pins[0] == '1':
    print('No')
else:
    line3 = '0'
    line4 = '0'
    line5 = '0'
    if pins[0] == '1' or pins[4] == '1':
        line4 = '1'
    if pins[1] == '1' or pins[7] == '1':
        line3 = '1'
    if pins[2] == '1' or pins[8] == '1':
        line5 = '1'

    rePins = [pins[6],pins[3],line3,line4,line5,pins[5],pins[9]]

    c = 0
    b = False

    for i in range(7):
        pin = rePins[i]

        if pin == '1' and b == False:
            c += 1
            b = True
        elif pin == '1' and b:
            b = True
        if pin == '0':
            b = False

    if c >= 2:
        print('Yes')
    else:
        print('No')