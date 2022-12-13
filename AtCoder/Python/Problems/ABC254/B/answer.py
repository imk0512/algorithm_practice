n = int(input())

list = [[1 for i in range(n)]for j in range(n)]

for i in range(1,n + 1):
    if(n + 1 == i):
        break
    char = ''
    for j in range(i):
        if j == 0:
            char += '1'
        elif  j + 1 == i:
            char += ' '
            char += '1'
        else:
            char += ' '
            num = list[i - 2][j - 1] + list[i - 2][j]
            list[i - 1][j] = num
            char += str(num)
    print(char)