from itertools import product

with open('input.txt', 'r') as f:
    input = f.read().split('\n')
    nums = [int(i) for i in input]
    for x, y in product(nums, nums):
        if (x + y == 2020):
            print(x * y)
            break

    for x, y, z in product(nums, nums, nums):
        if (x + y + z == 2020):
            print(x * y * z)
            break

