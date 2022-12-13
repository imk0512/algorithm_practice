N = int(input())

S =list(input().split())

pool = []
output = []

for i in range(len(S)):
    if i == 0:
        output.append(int(S[i]))
    else:
        output.append(int(S[i]) - int(S[i-1]))
print(' '.join(map(str,output)))