from copy import deepcopy

commands = []
with open('input.txt', 'r') as file:
    for i, line in enumerate(file):
        command = line.split(' ')
        commands.append([i, command[0], int(command[1]), False])


def run_program(commands):
    cmds = deepcopy(commands)
    acc = 0
    index = 0

    while True:
        command = cmds[index]
        cmd, value = command[1], command[2]
        if (command[3]):
            break

        cmds[index][3] = True

        if (cmd == 'acc'):
            acc += value
            index += 1
        elif (cmd == 'jmp'):
            index += value
        elif (cmd == 'nop'):
            index += 1
    return acc


def run_program2(commands):
    nops_and_jmps = []

    for c in commands:
        if (c[1] == 'nop' or c[1] == 'jmp'):
            nops_and_jmps.append([c[0], c[1]])

    for c in nops_and_jmps:
        cmds = deepcopy(commands)
        acc = 0
        index = 0

        while True:
            command = cmds[index]
            cmd, value = command[1], command[2]
            if (command[3]):
                break

            if (index == c[0]):
                if (cmd == 'jmp'):
                    cmd = 'nop'
                elif (cmd == 'nop'):
                    cmd = 'jmp'

            cmds[index][3] = True

            if (cmd == 'acc'):
                acc += value
                index += 1
            elif (cmd == 'jmp'):
                index += value
            elif (cmd == 'nop'):
                index += 1

            if (index == len(cmds) - 1):
                return acc


print(run_program(commands))
print(run_program2(commands))
