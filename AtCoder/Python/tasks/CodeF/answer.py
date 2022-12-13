import string

alphabets = string.ascii_lowercase

round = int(input())
lists = list(input() for s in range(round))

for s in lists:
    # round n
    
    # setup
    chars = list(s)
    intChars = []
    # aba
    # ['a','b','a']
    #  ↓
    # [1, 2, 1]
    # [{1: 'a'}, {2: 'b'}, {1: 'a'}]
    for s in chars:
        intChars.append(alphabets.index(s) + 1)
        #intChars.append({alphabets.index(s) + 1:s})

    # Alice select Max 
    asm = len(chars) // 2 * 2
    intChars.sort(reverse=True)
    AliceScore = sum(intChars[0:asm])
    BobScore = sum(intChars[asm: len(intChars)])
    
    if AliceScore > BobScore:
        print(f'Alice {AliceScore-BobScore}')
    elif BobScore > AliceScore:
        print(f'Bob {BobScore-AliceScore}')
  



# #　charList = [1, 2, 1] lmit = 2
# # [{1: 'a'}, {2: 'b'}, {1: 'a'}] keyList
# def max_sum(lmit, charList):
#     dp = [0] * (lmit + 1)
#     #selected = {}
#     for i in range(lmit):
#         print(f'dp[{i}] -> {dp[i]} a[{i}] -> { charList[i]}')
#         # dp[i + 1] = max(dp[i], dp[i] + a[i])
#         # ↓ 分解
#         if dp[i] > dp[i] + charList[i]:
            
#             dp[i + 1] = dp[i]
#         elif dp[i] < dp[i] + charList[i]:
#             dp[i + 1] = dp[i] + charList[i]

       
#     print('dp->',dp)
#     return dp[lmit]
