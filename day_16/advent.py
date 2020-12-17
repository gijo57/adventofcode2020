import re

with open('input.txt', 'r') as file:
    text = file.read().split('\n\n')
    rules = text[0].split('\n')
    my_ticket = text[1].split('\n')
    nearby_tickets = text[2]
    nearby_ticket_values = re.findall('(\d+)', nearby_tickets)
    valid_values = []

    for rule in rules:
        limits = re.findall('(\d+)', rule)
        valid_values.extend(list(range(int(limits[0]), int(limits[1])+1)))
        valid_values.extend(list(range(int(limits[2]), int(limits[3])+1)))

    valid_values = set(valid_values)
    invalid_values = []

    for value in nearby_ticket_values:
        value = int(value)
        if (value not in valid_values):
            invalid_values.append(value)

    answer = sum(invalid_values)
    print(answer)
