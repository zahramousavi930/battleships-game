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