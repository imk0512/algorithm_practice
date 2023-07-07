import sys
from collections import deque

# python3 answer.py < input.txt
# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def closest_num(num, num_list):
    return min(num_list, key=lambda x: abs(x-num))


def bfs(s:int,g:int):

    visited = set()  # 訪れた頂点を保存するセット
    queue = deque([[s]])
    visited.add(s)
    cnt = 0
    while True:
        cnt += 1
        for _ in range(len(queue)):
            # print(queue)
            vertex = queue.popleft()
            for num in vertex:
                a1 = num + 1
                a2 = num - 1
                a3 = num * 2

                nowRow = []
                if a1 not in visited:
                    nowRow.append(a1)
                    visited.add(a1)
                if a2 not in visited:
                    nowRow.append(a2)
                    visited.add(a2)
                if a3 not in visited:
                    if a3 <= (g * 2):
                        nowRow.append(a3)
                        visited.add(a3)
                # queue.append([find_nearest_number(nowRow,g)])
                queue.append(nowRow)
        
        if g in visited:
            print(cnt)
            break
    pass
# -------------------------------


# Please write the code below ---
def main():
    s, g = mv(int)
    if s == g:
        print(0)
    else :
        bfs(s,g)
    pass

# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------