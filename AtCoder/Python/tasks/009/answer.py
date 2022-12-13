# a,b = map(int,input().split())
# lists = list(map(int,input().split()))

# c = 0
# for i in range(len(lists)):
#     for l in range(len(lists)):
#         if l == 0:
#             continue
#         if lists[i] + lists[l] == b:
#             print('yes')
#             c += 1
#             break
# if c == 0:
#     print('No')

def f():return list(map(int,input().split()))
 
 
n,s=f()
A=f()
dp=[[0]*(s+1)for _ in range(n+1)]
dp[0][0]=1
print(dp)

for i in range(n):
	for j in range(s+1):
		dp[i+1][j]|=dp[i][j]
		if j>=A[i]:
			dp[i+1][j]|=dp[i][j-A[i]]