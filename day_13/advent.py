with open('input.txt', 'r') as file:
    text = file.readlines()
    earliest_departure = int(text[0].strip('\n'))
    buses2 = [bus for bus in text[1].split(',')]
    buses = [int(bus) for bus in buses2 if bus.isdigit()]

    earliest_bus = 0
    smallest_wait = earliest_departure

    for bus in buses:
        remainder = bus - (earliest_departure % bus)
        if (remainder < smallest_wait):
            earliest_bus = bus
            smallest_wait = remainder
        elif (remainder == 0):
            earliest_bus = bus
            break

    departure = earliest_departure + smallest_wait
    waiting_time = departure - earliest_departure
    answer = earliest_bus * waiting_time

    for bus in buses2:
        print(bus)

print(answer)