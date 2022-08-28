import random
import string
import os
import sys
from random import randint


size = 0
username = ''
scores = scores = {"computer": 0, "player": 0};

def random_spots(garid_size):
    
    x = randint(0, garid_size - 1)
    y = randint(0, garid_size - 1)
    return (x, y)


def valid_spots(x, y, grid_size):
   
    if 0 <= x < grid_size and 0 <= y < grid_size:
        return True

    return False

class Game_Board:
    
    def __init__(self, size, name, player=False):
        self.size = size
        self.num_ships = size
        self.name = name
        self.player = player
        self.ships = []
        self.guesses = []
        self.populate()
        
    def print(self):
        
        print(f"{self.name}'s Game_Board:")
        for row in self.board:
            print(" ".join(row))

    def guess(self, x, y):
        
        self.guesses.append((x, y))
        self.board[x][y] = "X"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return True
        else:
            return False

    def already_guessed(self, x, y):
        
        if (x, y) in self.guesses:
            return True
        return False

    def last_guess(self):
        
        return self.guesses[-1]

    def populate(self):
       
        board = [["." for x in range(self.size)] for y in range(self.size)]
        self.board = board
        for _ in range(self.num_ships):
            x, y = random_spots(self.size)
            while (x, y) in self.ships:
                x, y = random_spots(self.size)
            self.ships.append((x, y))
            if self.player:
                self.board[x][y] = "@"
# View Game Guide
def view_game_guide():
    view_guide = input(' >>> show game guides? (yes/no):\n')

    if view_guide == 'yes':
        print(GUIDES)
        enter_name()
    elif view_guide == 'no':
        enter_name()
    else:
        print(
            ' Please enter yes or no to select if you would'
            ' like to show the guide.')
        view_game_guide()

# Instructions
GUIDES = """
 Game Guides
1. To start the game, enter a user name.
2. Determine the size of the board,
- Small - Grid size = 5x5 - Hidden ships = 5
- Large - Grid size = 10x10 - Hidden ships = 10
3. When prompted, guess an x and y coordinate.
- Coordinates must be numbers between
- 1 and 5 on a small board
- 1 and 10 on a large board
4. Continue entering guesses until all ships are found.
5. When the game is finished, enter y (yes) or
When prompted, type n (no).
To exit the game, enter 'exit' at any time.
"""
def enter_name():
    global player_name
    player_name = input(' >>> Put your name here:\n')
    if player_name == 'exit':
        end_game()

    if player_name == '':
        print('Name not entered.')
        enter_name()
    else:
        if any(char in string.punctuation for char in player_name):
            print('Name has a special character in it,'
                  'Please only use letters.')
            enter_name()
        elif any(char.isdigit() for char in player_name):
            print('Use only letters if the name contains a number.')
            enter_name()
        else:
            select_board_size()

            def end_game():
    print('Thank you for playing')
    sys.exit()

view_game_guide();