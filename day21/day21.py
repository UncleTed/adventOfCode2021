
player_1_position = 7
player_2_position = 10
player_1_score = 0
player_2_score = 0

def roll_die():
    i = 1
    while 1:
        yield i
        i += 1
        if i > 100:
            i = 1


roll = roll_die()
number_of_die_rolls = 0
# while (player_1_score < 1000 and player_2_score < 1000):
# for i in range(6):
while 1:
    three_die_rolls = next(roll) + next(roll) + next(roll)
    number_of_die_rolls += 3
    if((player_1_position + three_die_rolls) % 10 == 0):
        player_1_position = 10
    else:
        player_1_position = (player_1_position + three_die_rolls) % 10
    player_1_score += player_1_position

    print(f'p1 position: {player_1_position} p1 score: {player_1_score}')
    if(player_1_score >= 1000):
        print(f'player 1 wins!')
        print(f'{number_of_die_rolls} * {player_2_score} = {number_of_die_rolls * player_2_score}')
        break

    three_die_rolls = next(roll) + next(roll) + next(roll)
    number_of_die_rolls += 3
    if((player_2_position + three_die_rolls) % 10 == 0):
        player_2_position = 10
    else:
        player_2_position = (player_2_position + three_die_rolls) % 10
    player_2_score += player_2_position
    print(f'p2 position: {player_2_position} p2 score: {player_2_score}')
    if(player_2_score >= 1000):
        print(f'player 2 wins!')
        print(f'{number_of_die_rolls} * {player_1_score} = {number_of_die_rolls * player_1_score}')
        break

    
print(f'number of die rolls: {number_of_die_rolls}')