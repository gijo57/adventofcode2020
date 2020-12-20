input = [14,3,1,0,9,5]


def solve_number(input, n):
    prevs = {}
    currs = {}
    for i in range(n):
        if (i < len(input)):
            currs[input[i]] = i+1
            num = input[-1]
        else:
            if (num in prevs):
                num = currs[num] - prevs[num]
                if (num in currs):
                    prevs[num] = currs[num]
                    currs[num] = i+1
                else:
                    currs[num] = i+1
            else:
                num = 0
                if (num in currs):
                    prevs[num] = currs[num]
                    currs[num] = i+1
                else:
                    currs[num] = i+1
    return num

answer = solve_number(input, 2020)
answer2 = solve_number(input, 30000000)
print(answer, answer2)
