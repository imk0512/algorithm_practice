nums = lists = list(map(int,input().split())) 

# スライム　デフォルト値
A = nums[0]
# スライム　最大数
B = nums[1]
# スライム　増殖倍率
K = nums[2]

count = 0
while A < B:
    A = A * K
    count += 1

print(count)