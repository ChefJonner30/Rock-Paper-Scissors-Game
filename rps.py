import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']


while True:
    user_input = input('Type Rock/Paper/Scissors or Q to quit: ').lower()
    if user_input == 'q':
        break

    if user_input not in options:
        error_message = print('Not a valid input')
        continue

    random_number = random.randint(0, 2)
    # 0 = rock, 1 = paper, 2 = scissors

    computer_pick = options[random_number]
    print(f'The computer picked {computer_pick}.')

    if user_input == 'rock' and computer_pick == 'scissors':
        print('You won!')
        user_wins += 1
    elif user_input == 'paper' and computer_pick == 'rock':
        print('You won!')
        user_wins += 1
    elif user_input == 'scissors' and computer_pick == 'paper':
        print('You won!')
        user_wins += 1
    else:
        print('You lost!')
        computer_wins += 1

if user_wins > computer_wins:
    winner = 'The overall winner is the user'
elif computer_wins > user_wins:
    winner = 'The overall winner is the computer'
elif user_wins == computer_wins:
    winner = 'The game resulted in a tie'

if user_wins > 0 or computer_wins > 0:
    print(
        f'You won {user_wins} amount of times. The computer won {computer_wins} amount of times. {winner}.')
else:
    print('Goodbye!')
