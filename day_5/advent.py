data = open('input.txt')
seat = 'FBFBBFFRLR'
seat_ids = []
my_id = 0


def search(high, data):
    low_bound = 0
    high_bound = high

    for char in data:
        if char in ['F', 'L']:
            high_bound = low_bound + (high_bound - low_bound) / 2
        elif char in ['B', 'R']:
            low_bound += (high_bound - low_bound) / 2
    return high_bound - 1


for row in data:
    seat_ids.append(int(search(128, row[:7]) * 8 + search(8, row[7:])))

for id in range(0, max(seat_ids)):
    if id not in seat_ids and id - 1 in seat_ids and id + 1 in seat_ids:
        my_id = id

print(max(seat_ids), my_id)
