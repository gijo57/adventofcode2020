with open('input.txt', 'r') as file:
    facing = 'E'
    directions = ['N', 'E', 'S', 'W']
    moves = {
        'N': 0,
        'E': 0,
        'S': 0,
        'W': 0
    }

    for line in file:
        direction = line[0]
        length = int(line[1:])
        if (direction == 'F'):
            moves[facing] += length
        elif (direction == 'R'):
            turns = int(length/90)
            facing = directions[(directions.index(facing)+turns) % len(directions)]
        elif (direction == 'L'):
            turns = int(length/90)
            facing = directions[directions.index(facing)-turns]
        else:
            moves[direction] += length

NS = moves['N'] - moves['S']
EW = moves['E'] - moves['W']

answer1 = abs(NS) + abs(EW)
print(answer1)