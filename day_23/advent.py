from copy import deepcopy

cups = [3, 8, 9, 1, 2, 5, 4, 6, 7]
min_label, max_label = min(cups), max(cups)
for i in range(1):
    current = 8
    current_cup = cups[current]
    destination_cup = current_cup-1
    pick_up_start, pick_up_end = current+1, current+4
    pick_up = []
    if (pick_up_start > len(cups)-1):
        pick_up_start = pick_up_start % (len(cups)-1)
    if (pick_up_end > len(cups)-1):
        pick_up_end = pick_up_end % (len(cups)-1)
    print(pick_up_start, pick_up_end)
    while (destination_cup in pick_up):
        destination_cup -= 1
        break
        if (destination_cup < min_label):
            destination_cup = max_label
    destination = cups.index(destination_cup)
    #print(pick_up)