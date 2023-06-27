import sys

# python3 answer.py < input.txt
# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def count_armors(materials, target):
    count = 0
    combinations = set()

    for material in materials:
        complement = target - material
        if complement in combinations:
            count += 1
        combinations.add(material)

    return count

# -------------------------------


# Please write the code below ---
def main():
    n = int(ip())
    m = int(ip())
    line = lmv(int)
    result = count_armors(line, m)
    print(result)
    
    pass
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------