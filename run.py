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
    
def select_board_size():
    global size
    print(' Hey ' + player_name)
    print("""
     choosing a board size,
     - Small
        - Grid size = 5x5
        - Hidden ships = 5
     - Large
        - Grid size = 10x10
        - Hidden ships = 10
    """)
    board_size = input(' >>> Enter S for small or L for large:\n')

    if board_size == 'L':
        size = 10
    elif board_size == 'S':
        size = 5
    else:
        print('Please try once more using a different option.')
        select_board_size()

    create_board()

def create_board():
    os.system('clear')

    temporary_board = Game_Board(size , "Computer", player=False)
    global uc_board;
    uc_board = temporary_board
    print("-" * 45)
    temporary_board = Game_Board(size, player_name, player=True)
    global user_board ;
    user_board = temporary_board
    play_game()

    def play_game():
    tunrs = size*2
    while True:
        show_boards()
        
        # player guess
        x, y = make_guess()
        while not valid_guess(x, y):
            x, y = make_guess()
        player_hit = uc_board.guess(x, y)

        # computer guess
        x, y = random_spots(size)
        while user_board.already_guessed(x, y):
            x, y = random_spots(size)
        computer_hit = user_board.guess(x, y)

        # end of round
        round_tally(player_hit, computer_hit)
        
        if tunrs <= 1:
            print("GAME OVER YOUR TUNRS ARE OUT")
            break
        print("You have " + str(tunrs) + " turns remaining")
        tunrs -= 1

def make_guess():
       
        while True:
            try:
                print("-" * 45)
                x = input("Guess a row:\n")
                x = int(x)
                y = input("Guess a column:\n")
                y = int(y)
                break
            except ValueError:
                print("Both the row and column must be numbers.")

        return (x, y)

def show_boards():
    
    uc_board.print()
    user_board.print()

def valid_guess( x, y):
    
    if not valid_spots(x, y, size):
        print(f"Row and column must be between 0 and {size - 1}")
        return False
    if uc_board.already_guessed(x, y):
        print("The same coordinates cannot be predicted more than once.")
        return False

    return True

def game_over():
    
    if scores["player"] >= size or \
        scores["computer"] >= size:
        return True
    return False

def round_tally(player_hit, computer_hit):
    print("-" * 45)
    print(f"{user_board.name} guessed " +
            f"{uc_board.last_guess()}")
    if player_hit:
        scores["player"] += 1
        print("That was a hit!")
    else:
        print("That was a miss!")
    print(f"Computer guessed {user_board.last_guess()}")
    if computer_hit:
        scores["computer"] += 1
        print("That was a hit!")
    else:
        print("That was a miss!")
    print("\nThe results after this round are:")
    print(f"{user_board.name}:" +
            f"{scores['player']} . Computer:{scores['computer']}")
    print("-" * 45)

view_game_guide();