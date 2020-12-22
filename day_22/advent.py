from collections import deque

with open('input.txt', 'r') as file:
    text = file.read().split('\n\n')
    player1 = deque([int(card) for card in text[0].split('\n')[1:]])
    player2 = deque([int(card) for card in text[1].split('\n')[1:]])

    while len(player1) and len(player2) > 0:
        player1_card = player1.popleft()
        player2_card = player2.popleft()

        if (player1_card > player2_card):
            player1.extend([player1_card, player2_card])
        elif (player1_card < player2_card):
            player2.extend([player2_card, player1_card])

    winner = ''
    if (len(player1) == 0):
        winner = player2
    elif (len(player2) == 0):
        winner = player1

answer = 0
for i in range(len(winner)):
    answer += (i+1) * (winner[len(winner)-i-1])

print(answer)
