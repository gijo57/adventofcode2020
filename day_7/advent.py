import re

file = open('input.txt', 'r')
lines = file.readlines()
pattern = r'((?:\S+\s+)(?:\S+))\s+bags?'
bags = [re.findall(pattern, line) for line in lines]
bag_dict = {}
for b in bags:
    bag_dict[b[0]] = b[1:]


def check_contents(root, bag):
    print(root, bag)
    contents = bag[1]
    if ('shiny gold' in contents):
        return root
    else:
        for i in contents:
            if (i in bag_dict.keys()):
                bag = (i, bag_dict[i])
                return check_contents(root, bag)


legit_bags = []

for bag in bag_dict.items():
    check_contents(bag[0], bag)

answer = len(set(legit_bags))
