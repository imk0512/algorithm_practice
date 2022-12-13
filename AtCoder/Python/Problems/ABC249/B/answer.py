
str = input()
strs = list(str) 
def has_duplicates(seq):
    return len(seq) != len(set(seq))


resulut = has_duplicates(strs)
low = str.islower()
up = str.isupper()

if resulut == False and low == False and up == False:
    print('Yes')
else:
    print('No')
