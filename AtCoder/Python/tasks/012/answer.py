import math

number = int(input())

## 素数判定
def trial_division(target):
    dest = int(math.sqrt(target))

    for i in range(2, dest):
        if target % i == 0:
            print("No")
            return
    print("Yes")


trial_division(number)
