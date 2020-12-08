commands = []
with open('input.txt', 'r') as file:
    for i, line in enumerate(file):
        command = line.split(' ')
        commands.append([i, command[0], int(command[1]), False])


def run_program(commands):
    acc = 0
    index = 0
    while True:
        command = commands[index]
        cmd, value = command[1], command[2]
        if (command[3]):
            break

        commands[index][3] = True

        if (cmd == 'acc'):
            acc += value
            index += 1
        elif (cmd == 'jmp'):
            index += value
        elif (cmd == 'nop'):
            index += 1
    return acc


print(run_program(commands))
