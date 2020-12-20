from itertools import product

differences = []

with open('input.txt', 'r') as file:
    joltages = sorted([int(joltage.strip('\n')) for joltage in file.read().split('\n')])
    outlet_joltage = 0
    device_joltage = max(joltages) + 3
    joltages.insert(0, outlet_joltage)
    joltages.append(device_joltage)

    for i, j in enumerate(joltages):
        if (i > 0):
            differences.append(j - joltages[i-1])

    answer = differences.count(1) * differences.count(3)

print(answer)
