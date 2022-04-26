
strs = list(int,input()) 
constList = ['0','1','2','3','4','5','6','7','8','9']
result = list(set(constList) - set(strs))

print(result)