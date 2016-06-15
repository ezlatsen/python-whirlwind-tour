import random

class Game(object):

    __CHOICES = { 
        1: 'Rock',
        2: 'Paper',
        3: 'Scissors',
        4: 'Lizard',
        5: 'Spock'
    }

    __RULES = { 
        1: [3, 4],
        2: [1, 5],
        3: [2, 4],
        4: [2, 5],
        5: [1, 3]
    }

    def __init__(self):
        self._player = None
        self._cpu = None
        self._winner = None
        self._plays = 0

    @property
    def player(self):
        return self.__CHOICES.get(self._player, None)
    
    @property
    def computer(self):
        return self.__CHOICES.get(self._cpu, None)
    
    @property
    def choices(self):
        return self.__CHOICES.values()

    @property
    def winner(self):
        return self._winner

    def __get_user_input(self):
        menu = '(1) Rock, (2) Paper, (3) Scissors, (4) Lizard, (5) Spock  >  '
        while True:
            user_guess = raw_input(menu)
            if str(user_guess) in ['1', '2', '3', '4', '5']:
                self._player = int(user_guess)
                return

    def play(self):
        self._cpu = random.randint(1,6)
        self.__get_user_input()
        if self._player == self._cpu:
            self._winner = 'Nobody'
        elif self._cpu in self.__RULES[self._player]:
            self._winner = 'Player'
        else:
            self._winner = 'Computer'
        self._plays += 1
        return self._winner

def main():
    g = Game()
    g.play()
    print('%s vs. %s' % (g.player, g.computer))
    print('The winner is, %s ' % g.winner)

if __name__ == '__main__':
    main()
