from itertools import combinations
preamble = 25


def find_sum(n, numbers):
    pairs = []
    pairs += combinations(numbers, 2)
    results = []
    for pair in pairs:
        if (pair[0] != pair[1]):
            results.append(pair[0] + pair[1] == n)
        else:
            results.append(False)

    return True in results


with open('input.txt', 'r') as f:
    numbers = [int(n) for n in f.read().split('\n')]
    answer = 0
    answer2 = 0

    for i, n in enumerate(numbers[preamble:]):
        if (not find_sum(n, numbers[i:i+preamble])):
            answer = n
            break

    for i in range(len(numbers)):
        nums = []
        total = 0
        for n in numbers[i:]:
            if (total < answer):
                nums.append(n)
                total += n
            elif (total == answer and len(nums) > 1):
                break
        if (total == answer):
            nums.sort()
            answer2 = nums[0] + nums[-1]
            break

print(answer, answer2)
