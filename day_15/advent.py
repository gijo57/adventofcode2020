input = [0, 3, 6]
turns_dict = {}

for i, value in enumerate(input):
    if (i != len(input)-1):
        turns_dict[value] = [i+1]
    else:
        turns_dict[value] = []

previous_number = input[-1]
spoken_number = 0

for i in range(len(input)+1, 8):

print(turns_dict)
