N, K = map(int,input().split())
list = input().split()



for i in range(K):
    if i > N:
        break
    list.pop(0)
    list.append('0')

print(' '.join(list))