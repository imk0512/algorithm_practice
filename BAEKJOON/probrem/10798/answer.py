import sys

# python3 answer.py < input.txt
# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def str_to_list(s:str):
    return [x for x in s]
def get_value_at_index(lst, index, default=None):
    try:
        return lst[index]
    except IndexError:
        return default
# -------------------------------


# Please write the code below ---
def main():
    resource = []
    lenCnt = 0
    while True:
        line = str_to_list(ip())
        if len(line) == 0:
            break
        if len(line) >= lenCnt:
            lenCnt = len(line)
        resource.append(line)

    
    ans = ''
    for i in range(lenCnt):
        for j in range(len(resource)):
            if not get_value_at_index(resource[j],i):
                continue
            ans += resource[j][i]
    print(ans)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------