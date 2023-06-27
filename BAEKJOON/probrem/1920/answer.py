import sys

# python3 answer.py < input.txt
# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def binary_search(sorted_list, search_value: int) -> bool:
    left_index: int = 0
    right_index: int = len(sorted_list) - 1
    while left_index <= right_index:
        middle_index: int = (left_index + right_index) // 2
        middle_value: int = sorted_list[middle_index]

        if search_value < middle_value:
            right_index = middle_index - 1
            continue
        if search_value > middle_value:
            left_index = middle_index + 1
            continue

        return True

    return False
# -------------------------------


# Please write the code below ---
def main():
    n = int(ip())
    nLine = list(set(lmv(int)))
    m = int(ip())
    mLine = lmv(int)
    
    nLine.sort()
    for v in mLine:
        if binary_search(nLine,v):
            print(1)
        else:
            print(0)
    pass
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------