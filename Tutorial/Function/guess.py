from get_int import get_int
import random

min_value = 1
max_value = 20
answer = random.randint(min_value, max_value)
guess = get_int(f"請在{min_value} - {max_value}中猜一個數字: ")
while answer != guess:
    if answer > guess:
        print("太小了")
    else:
        print("太大了")
    guess = get_int(f"請在{min_value} - {max_value}中猜一個數字: ")
print("答對了")
