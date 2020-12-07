import re

file = open('input.txt', 'r')
lines = file.readlines()
pattern = r'^(\w+\s\w+)\s\w+\s\w+\s\w+\s(\w+\s\w+)\s\w+,\s\d\s(\w+\s\w+)'
bags = list(filter(None, [re.findall(pattern, l) for l in lines]))
bags = [b[0] for b in bags]
main_bags = [bag[0] for bag in bags]