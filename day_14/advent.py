import re
import numpy as np


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
    return(masked_address)


with open('input.txt') as file:
    memory = {}
    mask = ''
    for line in file:
        if ('mask' in line):
            mask = line.split(" = ")[1].strip('\n')
        else:
            address = re.search('\d+', line.split(' = ')[0])[0]
            value = int(line.split(" = ")[1].strip('\n'))
            memory[address] = mask_value(mask, value)

    answer = sum(memory.values())
    #print(answer)


def mask_address(mask, address):
    mask = list(mask)
    binary = list(format(address, '036b'))
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
    
    print(masked_addresses)


print(mask_address('000000000000000000000000000000X1001X', 42))