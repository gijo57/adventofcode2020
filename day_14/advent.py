from os import replace
import re
from itertools import product


def replace_floating_bits(address, indices, combination):
    masked_address = address
    for i, j in enumerate(indices):
        masked_address[j] = str(combination[i])
    return ''.join(masked_address)


def mask_value(mask, value):
    mask = list(mask)
    binary = list(format(value, '036b'))

    masked_address = []
    for bits in zip(mask, binary):
        if (bits[0] == 'X'):
            masked_address.append(bits[1])
        else:
            masked_address.append(bits[0])
    masked_address = int(''.join(masked_address), 2)
    return masked_address


def mask_address(mask, address):
    mask = list(mask)
    binary = list(format(int(address), '036b'))
    masked_address = []

    for bits in zip(mask, binary):
        if (bits[0] == '0'):
            masked_address.append(bits[1])
        elif(bits[0] == '1'):
            masked_address.append(bits[0])
        else:
            masked_address.append('X')

    masked_addresses = []
    floating_bit_indices = [i for i, b in enumerate(masked_address) if b == 'X']
    floating_bit_combinations = list(product([0, 1], repeat=len(floating_bit_indices)))

    for c in floating_bit_combinations:
        masked_addresses.append(replace_floating_bits(masked_address, floating_bit_indices, c))

    return [int(a, 2) for a in masked_addresses]


with open('input.txt') as file:
    memory = {}
    memory2 = {}
    mask = ''
    for line in file:
        if ('mask' in line):
            mask = line.split(" = ")[1].strip('\n')
        else:
            address = re.search('\d+', line.split(' = ')[0])[0]
            value = int(line.split(" = ")[1].strip('\n'))
            memory[address] = mask_value(mask, value)
            addresses = mask_address(mask, address)

            for a in addresses:
                memory2[a] = value

answer = sum(memory.values())
answer2 = sum(memory2.values())
print(answer, answer2)
