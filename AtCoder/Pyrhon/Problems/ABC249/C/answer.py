N,y = map(int,input().split())
lists = [input() for i in range(x)]

# N <= 15 最大　文字列個数 S1 ~ S15まで
# 2 ** 15 = 32768  << 最大パターン

for i in range(N):
    charList = list(lists[i])
    
