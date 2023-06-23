import sys

# python3 answer.py < input.txt
# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def original_distance(n):
    n = str(n)[::-1]  # Reverse the number for easier calculation
    distance = 0
    power = 0
    for digit in n:
        digit = int(digit)
        if digit >= 5:
            digit -= 1  # Adjust the digit if it is greater than or equal to 5
        distance += digit * (9 ** power)  # Calculate the original distance
        power += 1
    return distance

# -------------------------------


# Please write the code below ---
def main():
    n = int(input().strip())
    print(original_distance(n))
    pass
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------