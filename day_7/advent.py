import re

file = open('input.txt', 'r')
lines = file.readlines()
pattern = r'((?:\S+\s+)(?:\S+))\s+bags?'
bags = [re.findall(pattern, line) for line in lines]
bag_dict = {}
for b in bags:
    bag_dict[b[0]] = b[1:]


def check_contents(original_root, bag):
    root = bag[0]
    contents = bag[1]

    if ('shiny gold' in contents):
        return root
    else:
        for b in contents:
            if (b in bag_dict.keys()):
                bag = (b, bag_dict[b])
                return check_contents(original_root, bag)


legit_bags = []

for bag in bag_dict.items():
    legit_bags.append(check_contents(bag, bag))

legit_bags = [b for b in legit_bags if b is not None]
answer = len(legit_bags)
print(legit_bags, answer)
