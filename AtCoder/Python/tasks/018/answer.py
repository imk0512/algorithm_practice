N = int(input())
List = list(map(int, input().split()))
Dict = {100: 0, 200: 0, 300: 0, 400: 0}

for n in range(N):
    Dict[List[n]] += 1

Ans = Dict[100] * Dict[400] + Dict[200] * Dict[300]
print(Ans)
