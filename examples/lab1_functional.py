import random

def rps_validator(choice):
    """
    >>> rps_validator(1)
    True
    >>> rps_validator('1')
    True
    >>> rps_validator('dog')
    False
    """
    return str(choice) in ['1', '2', '3', '4', '5']

def get_user_input(message, validator):
    """
    Get user input and validate it. Can't doctest this because of input call
    """
    while True:
        user_guess = raw_input(message)  #  This works in 2.7x
        if validator(user_guess):
            return user_guess

def get_cpu_choice():
    """
    >>> 6 > get_cpu_choice() > 0
    True
    """
    return random.randint(1,5)

def get_winner(player, cpu):
    """
    >>> get_winner(1,3)
    'Player'
    >>> get_winner(1,2)
    'Computer'
    >>> get_winner(1,1)
    'Nobody'
    """
    rules = { 
        1: [3, 4],
        2: [1, 5],
        3: [2, 4],
        4: [2, 5],
        5: [1, 3]
    }
    if player == cpu:
        return 'Nobody'
    elif cpu in rules[player]:
        return 'Player'
    else:
        return 'Computer'

def main():
	menu = '(1) Rock, (2) Paper, (3) Scissors, (4) Lizard, (5) Spock  >  '
	choices = { 
	    1: 'Rock',
	    2: 'Paper',
	    3: 'Scissors',
	    4: 'Lizard',
	    5: 'Spock'
	}
	cpu = get_cpu_choice()
	player = get_user_input(menu, rps_validator)
	player = int(player)
	try:
		winner = get_winner(player, cpu)
	except (KeyError, ValueError):
		print('There was a problem with your input')
	else:
		print('%s vs. %s' % (choices[player], choices[cpu]))
		print('The winner is, %s ' % winner)

if __name__ == '__main__':
	main()
