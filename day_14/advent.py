import re


def mask_value(mask, value):
    mask = list(mask)
    binary = list(format(value, '036b'))

    masked_value = []
    for bits in zip(mask, binary):
        if (bits[0] == 'X'):
            masked_value.append(bits[1])
        else:
            masked_value.append(bits[0])
    masked_value = int(''.join(masked_value), 2)
    return(masked_value)


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
    print(answer)
