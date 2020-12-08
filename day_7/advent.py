import re

file = open('input.txt', 'r')
lines = file.readlines()
pattern = r'^(\w+\s\w+)\s.*\s(\w+\s\w+)\s\w+.*\s\d\s(\w+\s\w+)'
bags = [re.findall(pattern, line) for line in lines]
print(bags)
#bag_dict = {bag[0]: [bag[1], bag[2]] for bag in bags}
