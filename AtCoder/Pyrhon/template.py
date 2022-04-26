"""
入力値 >>> ABC
"""
str = input() # >>> str = "ABC"
strs = list(input()) # >>> strs = ["A","B","C"]

"""
入力値 >>> 1
"""
int = int(input()) # >>> int = 1

"""
入力値 >>> 1 2
"""
x,y = map(int,input().split()) # >>> x = 1, y = 2

"""
入力値 >>> 1 2 3 4 5 ... n
"""
lists = input().split() # >>> lists = ['1','2','3',...,'n']
lists = list(map(int,input().split())) # >>> lists = [1,2,3,4,5,...,n]

"""
入力値　>>> FTFTTFTTTFTTTTF 
"""
lists = input().split('T') 
# >>> list = ['F', 'F', '', 'F', '', '', 'F', '', '', '', 'F']

"""
入力値　>>> 3
           hoge
           foo
           bar
"""
num = int(input())
lists = [input() for i in range(n)]
# >>> num = 3
# >>> lists = ['hoge','foo','bar']

"""
入力値　>>> 1 2 2 3 1
           4 5 3 4 1 2 3 4
           2 3 5 6 0 2
"""
while True:
    try:
        lists = list(map(int,input().split())) 
        # ループ
        # 1周目　list = [1,2,2,3,1]
        # 2周目　list = [4,5,3,4,1,2,3,4]
        # 3周目　list = [2,3,5,6,0,2]
        # 4周目　エラー(out of range) よってexceptに行く。
    except:
        break;

# OR

lists = []
while True:
    try:
        lists.append(list(map(int,input().split())))
    except:
        break;
#lists = [[1, 2, 2, 3, 1], [4, 5, 3, 4, 1, 2, 3, 4], [2, 3, 5, 6, 0, 2]]


"""
入力値 >>> A B
"""

"""
入力値 >>> d1 d2 ... dN
&
入力値 >>> d1 
          d2 
          ...
          dN
"""


"""
入力値　>>> 3 4
           99 99 99
           99 0 99
           99 99 99
           99 99 99
"""


"""
入力値 >>> 10 12
          W........WW.
          .WWW.....WWW
          ....WW...WW.
          .........WW.
          .........W..
          ..W......W..
          .W.W.....WW.
          W.W.W.....W.
          .W.W......W.
          ..W.......W.
"""


"""
入力値 >>> d1 d2 .. d? （入力数が不明）
"""

