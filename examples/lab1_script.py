import random

menu = '(1) Rock, (2) Paper, (3) Scissors, (4) Lizard, (5) Spock  >  '
while True:
    user_guess = raw_input(menu)  #  This works in 2.7x
    if user_guess in ['1', '2', '3', '4', '5']:
        break
user_guess = int(user_guess)
cpu = random.randint(1,6)

choices = { 
    1: 'Rock',
    2: 'Paper',
    3: 'Scissors',
    4: 'Lizard',
    5: 'Spock'
}
rules = { 
    1: [3, 4],
    2: [1, 5],
    3: [2, 4],
    4: [2, 5],
    5: [1, 3]
}

if user_guess == cpu:
    print('Tie game')
elif cpu in rules[user_guess]:
    print('%s beats %s' % (choices[user_guess], choices[cpu]))
    print('The winner is, Player')
else:
    print('%s beats %s' % (choices[cpu], choices[user_guess]))
    print('The winner is, Computer')