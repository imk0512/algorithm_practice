# import math
# from collections import defaultdict


# 文字列１個
# N = input()
# 数値 1個
# num = int(input())
# 数値２個
R,C = map(int,input().split())
# 数値3個
# N,X,Y = map(int,input().split())

# リスト　文字列
# strList = list(map(input().split()))
# リスト　数値
# numList = list(map(int,input().split()))


list = []
list.append('###############')
list.append('#.............#')
list.append('#.###########.#')
list.append('#.#.........#.#')
list.append('#.#.#######.#.#')
list.append('#.#.#.....#.#.#')
list.append('#.#.#.###.#.#.#')
list.append('#.#.#.#.#.#.#.#')
list.append('#.#.#.###.#.#.#')
list.append('#.#.#.....#.#.#')
list.append('#.#.#######.#.#')
list.append('#.#.........#.#')
list.append('#.###########.#')
list.append('#.............#')
list.append('###############')

row = list[R-1]
print('black' if row[C-1] == '#' else 'white')