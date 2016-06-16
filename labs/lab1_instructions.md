# Lab 1: Rock-Paper-Scissors-Lizard-Spock

## Background

You are going to implement an enhanced version of the classic game 'Rock, Paper, Scissors". This time around we have added acouple new choices to keep things interesting... Lizard and Spock. The addition of these two choices will make writing the code a bit more difficult than the classic verisonof the game, so you will need some of the more advnaced datas structures (lists, dictionaries) to keep things as simple as possible.

## Rules

The game is an expansion on the game Rock, Paper, Scissors. Each player picks a variable and reveals it at the same time. The winner is the one who defeats the others. In a tie, the process is repeated until a winner is found.

- Scissors cuts Paper
- Paper covers Rock
- Rock crushes Lizard
- Lizard poisons Spock
- Spock smashes Scissors
- Scissors decapitates Lizard
- Lizard eats Paper
- Paper disproves Spock
- Spock vaporizes Rock
- Rock crushes Scissors

[![ROSHAMBHO](http://vignette1.wikia.nocookie.net/bigbangtheory/images/7/7d/RPSLS.png/revision/latest?cb=20120822205915)](https://www.youtube.com/watch?v=cSLeBKT7-sM)

## Requirements

- You play against the computer, and the computer must choose a hand randomly.
- You much display a menu with all the choices, the user must pick one
- If the human player does not choose a valid choice you must ask them to pick again.
- Develope the code required to determine who won the round
- In the case of a tie, you must play tie-breaker rounds until there is a winner
- Test your code by playing several rounds against the computer.

## Tips

- You can use data structures like dictionaries to provide "maps" for things like "rock beats scissors".
  - Don't forget the 'in' operator, it is your friend.
- Try encoding each encode each choice and doing some simple math instead of using data structures
