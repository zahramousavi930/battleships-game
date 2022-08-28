# Battleships

A Battleships Command terminal game for Python Users can compete with the computer by correctly estimating the position of their opponent's battleship before the machine locates its own. Each game allows players to choose the number of ships and board sizes they want to use.

Link to deployed website - [Battleships_Game](https://battleships-games.herokuapp.com/)

![responsive_screenshot](/picture/screenshot.png)


[Go to How to Play](#how-to-play)

[Go to Features](#features)
  - [Go to Existing Features](#existing-features)
  - [Go to Features Left to Implement](#features-left-to-implement)

[Go to Data Model](#data-model)

[Go to Testing](#testing)
  - [Go to Solved Bugs](#solved-bugs)
  - [Go to Remaining Bugs](#remaining-bugs)
  - [Go to Validator Testing](#validator-testing)

[Go to Deployment](#deployment)

[Go to Credits](#credits)

## How to Play

'Battleship' is the inspiration for Battleship Command. On [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game)), you may find out more information.

In this variation, the player chooses the board size, the number of ships for each player, and the player names before a random algorithm creates two boards.

A | symbol indicates that the player's ships may be seen, but the computer's ships cannot be seen.

Hits are displayed on the board with an O, whereas guesses are indicated with an X.

The computer will randomly create the player's next guess while they search for and scuttle each other's battleships using the row and column inputs they provided.

The winner is the player who locates and sinks all of their opponent's battleships first.

## Features

### Existing Features

#### __Key Features__

- All inputs are validated and checked for errors.

- You cannot enter coordinates outside the boundaries of the grid - All relevant inputs must have a name, a number, and a setting.
- You can only make one guess per entry.

- Generated randomly

- Within the confines of the game's settings, computer guesses and ship coordinates are created at random (shown below)

#### __Game Settings__

- The player name, board size option and number of ships for each player can all be entered in the game settings area.

- This part improves replay value by giving the user control over how they want to play.

![Game Settings](/picture/1.png)

#### __Board & Scores__

- Based on the game settings, the board and scores section shows player ship placements, current estimates and hits, and a remaining ship count for each player.

- This portion gives the player a visual representation of the state of the game as it is updated for guesses, hits, and scores after each round.

![Board & Scores](/picture/3.png)

#### __Player Guesses__

 - This section shows the player's previous guesses, confirms if the player would like to continue and receives input for the row and column of their next guess.

 - This section fundamentally allows the player to control how they play the game and allows them to start again before the game ends naturally.

 ![Player Guesses](/picture/4.png)

### Features Left to Implement

 - Allow players to place ships themselves

 - Enable ships large than 1x1

 ## Data Model

In this project I decided to implement a `GameArea` class. This class stores variables and hosts methods for creating the boards, ship coordinates, player ship placement, updating guesses and hits and declaring the game over.

The `GameArea` class is initially fed arguments from the settings variable which changes based upon the selections chosen by the player. This then updates each round through the `new_round` function and the seperate functions it calls e.g. `new_guess` and `generate_boards`.

These functions and methods collectively game critical variables which are updated by function's `return` values and displayed to the player through `print` statements.

## Testing

I manually tested this project by carrying out the subsequent actions:

- Verified there are no issues by running the code through a PEP8 linter.

- Given invalid inputs: strings when numbers are anticipated, inputs that are outside of boundaries, and numerous instances of the same guess.

- Tested in my local terminal and the Heroku terminal for the Code Institute.

### __Solved Bugs__

 - When writing the project, the guesses and hit lists were resetting after each round. I fixed this by refactoring these lists as part of the `GameArea` class

 - When writing the project, errors were occuring once a non duplicate guess was input after a duplicate guess attempt was made. I fixed this by changing the value to `None` if a duplicate was identified then adding a `while` loop if the returned guess result was `None`

 - Tuples from guesses list fed in to `update_board` could not be unpacked. This was fixed by changing the `for` loop to `_, guess enumerate(guesses)`

 ### __Remaining Bugs__

 - Boards, scores, hit confirmation and previous guesses cannot all be displayed on screen at once for larger board sizes due to line count limitation on terminal

### __Validator Testing__


Python - no errors found when passing through [PEP8 online](http://pep8online.com)

![pep8_results](/picture/chack.png)

## Deployment 

This project was deployed using Code Institute's mock terminal for Heroku.

 - Steps for deployment:

   - Run command `heroku login -i`, then input login credentials
   - Run command `heroku create battleships-command`
   - In the Heroku app, set buildpacks to `heroku/python` and `heroku/nodejs`
     - Buildpacks must be in this exact order
   - Run command `git push heroku main`

 - Additional Notes:

   - Due to an ongoing issue, the GitHub deployment method for Heroku is currently unavailable

## Credits

 - README structure used from [Sample README.md - Code Institute](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+PE_PAGPPF+2021_Q2/courseware/b3378fc1159e43e3b70916fdefdfae51/605f34e006594dc4ae19f5e60ec75e2e/)
 - Deployment terminal provided by [Code Institute](https://codeinstitute.net/)
 - Responsive design mockup tool by [Am I Responsive](https://ui.dev/amiresponsive)
 - Battleships game details by [Wikipedia](https://en.wikipedia.org/wiki/Main_Page)
 - Seperate lists code by [User648852 - Stack Overflow](https://stackoverflow.com/questions/13443588/how-can-i-format-a-list-to-print-each-element-on-a-separate-line-in-python)

 [Go back to top](#battleships-command)