from numpy import prod

with open('input.txt', 'r') as f:
    location_index = 0
    tree_count = 0
    for l in f:
        l = l.strip('\n')
        row_length = len(l)

        if (location_index > row_length - 1):
            location_index -= row_length
        location = l[location_index]
        if (location == "#"):
            tree_count += 1
        location_index += 3
print(tree_count)


def tree_counter(right, down):
    f = [l.strip('\n') for l in open('input.txt', 'r').readlines()]
    location_index = 0
    tree_count = 0

    for i in range(0, len(f), down):
        l = f[i]
        row_length = len(l)

        if (location_index > row_length - 1):
            location_index -= row_length
        location = l[location_index]
        if (location == "#"):
            tree_count += 1
        location_index += right
    return tree_count


result = prod([tree_counter(1, 1),tree_counter(3, 1),tree_counter(5, 1),tree_counter(7, 1),tree_counter(1, 2)])
print(result)