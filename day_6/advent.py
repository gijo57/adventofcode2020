answer_count, answer_count2 = 0, 0

with open('input.txt', 'r') as f:
    groups = [group for group in f.read().split('\n\n')]
    for g in groups:
        answers = len(set(g))
        if (g.count('\n') > 0):
            answer_count += answers - 1
        else:
            answer_count += answers

    for g in groups:
        answered_by_everyone = 0
        members = len(g.split('\n'))
        questions = list(''.join(g.split()))
        for char in set(questions):
            print(questions, char, members)
            if (questions.count(char) == members):
                answer_count2 += 1

print(answer_count, answer_count2)
