import numpy as np
import copy
import time

start = time.process_time()


def get_neighbor_states(seats, ix, iy):
    neighbors = 0
    for x in range(ix-1, ix+2):
        for y in range(iy-1, iy+2):
            if (ix == x and iy == y):
                continue
            if ((x >= 0 and y >= 0) and (x < int(seats.shape[0]) and y < int(seats.shape[1]))):
                if (seats[x,y] == '#'):
                    neighbors += 1
    return neighbors


def count_occupied_seats(seats):
    helper_seats = copy.deepcopy(seats)
    changed = 0

    for ix, iy in np.ndindex(seats.shape):
        seat = seats[ix, iy]
        occupied_neighbors = get_neighbor_states(seats, ix, iy)

        if (seat == 'L' and occupied_neighbors == 0):
            helper_seats[ix, iy] = '#'
            changed += 1
        if (seat == '#' and occupied_neighbors >= 4):
            helper_seats[ix, iy] = 'L'
            changed += 1

    if (changed == 0):
        return (helper_seats == '#').sum()
    else:
        return count_occupied_seats(helper_seats)


with open('input.txt', 'r') as file:
    seats = np.array([list(line.strip('\n')) for line in file])

answer = count_occupied_seats(seats)
print(answer)

end = time.process_time()
print(end - start)
