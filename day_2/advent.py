import re

#1 & #2
with open('input.txt', 'r') as f:
    lines = f.read().split('\n')
    count = 0
    count2 = 0

    for i, l in enumerate(lines):
        line = re.split('\W+', lines[i])
        min, max, char, pw = int(line[0]), int(line[1]), line[2], line[3]
        
        if (min <= pw.count(char) <= max):
            count += 1

        if (bool(pw[min-1] == char) ^ bool(pw[max-1] == char)):
            count2 += 1
        
print(count, count2)
