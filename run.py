# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


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

view_game_guide();