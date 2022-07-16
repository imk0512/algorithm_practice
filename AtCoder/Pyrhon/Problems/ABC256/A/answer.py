N,M,X,T,D = map(int,input().split())

if M >= X :
    print(T)
else:
    n = X - M
    hight = T - (D * n)
    print(hight)
