import difflib
# S = list(input())
# T = list(input())
S = input()
T = input()

# i = 0
# while(True):
#     if len(S) -1 < i:
#         print(i)
#         break
#     if S[i] != T[i]:
#         print(i+1)
#         break

#     i+=1

def diff(a,b):
    print(enumerate(difflib.ndiff(a, b)))
    for i,s in enumerate(difflib.ndiff(a, b)):
        print(i)
        print(s)
        if s[0]==' ': continue
        elif s[0]=='-':
            print(u'Delete "{}" from position {}'.format(s[-1],i))
        elif s[0]=='+':
            print(u'Add "{}" to position {}'.format(s[-1],i))

diff(S,T)