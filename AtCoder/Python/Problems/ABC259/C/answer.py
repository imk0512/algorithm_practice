def solve(S,T,cnt):
    print('S->',S)
    s_List = list(S)
    t_List = list(T)
    length =len(s_List)
    result = 'No'
    for i in range(cnt,length):
        print(length)
        if 1 <= i and i < length-1:
            if s_List[i] == s_List[i + 1]:
                if t_List[i] == t_List[i+1] and t_List[i] == s_List[i]:
                    s_List.insert(i + 1,s_List[i + 1])
                    if "".join(s_List) == T:
                        return "Yes"
                    #Sのi文字目とTのi文字目が同じ
                    solve("".join(s_List),T,length+1)
    return result

S = input()
T = input()

re = solve(S,T,0)

print(re)