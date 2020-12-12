from collections import deque

with open('input.txt', 'r') as file:
    facing = 'E'
    directions = ['N', 'E', 'S', 'W']
    moves = {
        'N': 0,
        'E': 0,
        'S': 0,
        'W': 0
    }
    ship_location = {
            'N': 0,
            'E': 0,
            'S': 0,
            'W': 0
    }
    waypoint_location = [1, 10, 0, 0]

    for line in file:
        direction = line[0]
        length = int(line[1:])
        if (direction == 'F'):
            moves[facing] += length
            ship_location['N'] += waypoint_location[0]*length
            ship_location['S'] += waypoint_location[2]*length
            ship_location['E'] += waypoint_location[1]*length
            ship_location['W'] += waypoint_location[3]*length
        elif (direction == 'R'):
            turns = int(length/90)
            facing = directions[(directions.index(facing)+turns) % len(directions)]
            new_location = deque(waypoint_location)
            new_location.rotate(turns)
            waypoint_location = list(new_location)
        elif (direction == 'L'):
            turns = int(length/90)
            facing = directions[directions.index(facing)-turns]
            new_location = deque(waypoint_location)
            new_location.rotate(-turns)
            waypoint_location = list(new_location)
        else:
            moves[direction] += length
            if (direction == 'N'):
                waypoint_location[0] += length
            elif (direction == 'S'):
                waypoint_location[2] += length
            elif (direction == 'E'):
                waypoint_location[1] += length
            elif (direction == 'W'):
                waypoint_location[3] += length

NS = moves['N'] - moves['S']
EW = moves['E'] - moves['W']

answer1 = abs(NS) + abs(EW)
answer2 = abs(ship_location['N']-ship_location['S'])+abs(ship_location['E']-ship_location['W'])

print(answer1, answer2)
