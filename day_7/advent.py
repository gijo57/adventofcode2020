import re

file = open('input.txt', 'r')
lines = file.readlines()
pattern = r'((?:\S+\s+)(?:\S+))\s+bags?'
bags = [re.findall(pattern, line) for line in lines]
bag_dict = {}
for b in bags:
    bag_dict[b[0]] = b[1:]


