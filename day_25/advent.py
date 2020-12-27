with open('input.txt', 'r') as file:
    text = file.readlines()
    card_pk, door_pk = int(text[0]), int(text[1])
    card_loop_size = 0
    value = 1

    while (value != card_pk):
        value *= 7
        value %= 20201227
        card_loop_size += 1

    value = 1
    for i in range(card_loop_size):
        value *= door_pk
        value %= 20201227   

print(value)