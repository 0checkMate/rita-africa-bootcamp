import random

def add_nums(a, b):
    sum = a + b
    return(sum)

nums = [4, 6, 9, 3, 7, 4]

a = random.choice(nums)
b = random.choice(nums)

total = add_nums(a,b)
print(total)