import pprint

N,X,Y,Z = map(int,input().split())
mathScore = list(map(int,input().split()))
englishScore = list(map(int,input().split()))



list=[[0]*5 for i in range(N)]
rank = []
for i in range(N):
    list[i][0] = mathScore[i]
    list[i][1] = englishScore[i]
    list[i][2] = mathScore[i] + englishScore[i]
    list[i][3] = N - i
    list[i][4] = i

print(list)


# 数学のソーと
sorted_data = sorted(list, key=lambda x:(x[0],x[3]), reverse=True)

if(X > 0):
    for i in range(X):
        val = sorted_data[i]
        rank.append(val[4] + 1)

    del sorted_data[0:X]

# 英語のソート
sorted_data1 = sorted(sorted_data, key=lambda x:(x[1],x[3]), reverse=True)

if(Y > 0):
    for j in range(Y):
        val = sorted_data1[j]
        rank.append(val[4] + 1)
    del sorted_data1[0:Y]

# 合計点ソート
sorted_data2 = sorted(sorted_data1, key=lambda x:(x[2],x[3]), reverse=True)

if(Z > 0):
    for a in range(Z):
        val = sorted_data2[a]
        rank.append(val[4] + 1)

rank.sort()
for s in rank:
    print(s)