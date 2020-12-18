import re
from collections import defaultdict
from numpy import prod


def diff(li1, li2):
    return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))


with open('input.txt', 'r') as file:
    text = file.read().split('\n\n')
    rules = text[0].split('\n')
    my_ticket = text[1].split('\n')
    my_ticket_values = [int(v) for v in my_ticket[1].split(',')]
    nearby_tickets = text[2]
    nearby_ticket_values = re.findall('(\d+)', nearby_tickets)
    valid_values = []
    valid_tickets = []
    rules_dict = {}

    for rule in rules:
        limits = re.findall('(\d+)', rule)
        valid_values.extend(list(range(int(limits[0]), int(limits[1])+1)))
        valid_values.extend(list(range(int(limits[2]), int(limits[3])+1)))

        rule_name = re.findall('(\w+|\w+\s\w+):', rule)[0]
        rules_dict[rule_name] = [range(int(limits[0]), int(limits[1])+1)]
        rules_dict[rule_name].extend([range(int(limits[2]), int(limits[3])+1)])

    valid_values = set(valid_values)
    invalid_values = []

    for value in nearby_ticket_values:
        if (int(value) not in valid_values):
            invalid_values.append(int(value))

    for ticket in nearby_tickets.split('\n')[1:]:
        ticket = ticket.split(',')
        if (not any(str(invalid) in ticket for invalid in invalid_values)):
            valid_tickets.append(ticket)

    field_locations = defaultdict(lambda: [])

    for rule in rules_dict:
        ranges = rules_dict[rule]
        for i in range(len(my_ticket[1].split(','))):
            ticket = [ticket for ticket in valid_tickets]
            fields = [field[i] for field in ticket]
            range_check = all([int(field) in ranges[0] or int(field) in ranges[1] for field in fields])
            if (range_check):
                field_locations[rule].append(i+1)

    sorted_fields = dict(sorted(field_locations.items(), key=lambda k: len(k[1])))

    final_fields = {}
    prev = ''

    for k, v in sorted_fields.items():
        if (len(v) > 1):
            val = diff(v, prev)
            final_fields[k] = val
        else:
            final_fields[k] = v
        prev = v

    answer_values = []

    for k in final_fields.keys():
        if ('departure' in k):
            answer_values.append(my_ticket_values[final_fields[k][0]-1])

    answer = sum(invalid_values)
    answer2 = prod(answer_values)
    print(answer, answer2)
