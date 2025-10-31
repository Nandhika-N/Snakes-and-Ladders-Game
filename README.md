# Snakes-and-Ladders-Game
Snakes and Ladders Game
Snakes and Ladders - Python Implementation

A complete text-based Snakes and Ladders game built in Python, progressing from simple variable setup to a fully functional, multi-player, feature-rich version with snakes, ladders, power tiles, and special rolls.

This project follows a structured learning path, where each stage introduces new programming concepts — variables, loops, conditionals, functions, data structures, and user interaction.

This Python project simulates a classic Snakes and Ladders game.
It starts from defining players and board setup and evolves into a full-featured game engine with:
Dynamic number of players (1–4)
Random dice rolls
Snakes and ladders logic
Win conditions
Turn-by-turn console gameplay
Surprise power tiles for advanced mechanics
Clean functional design and modularity
The final version of the game uses a dictionary-based structure for better readability and scalability.

Features

Multi-player support (1–4 players)
Snakes and ladders interactions
No moves beyond tile 100
Automatic winner detection
Manual and automated play modes
Surprise tiles and special rolls
Modular, function-driven structure

Game Rules

All players begin at position 0.
Each player rolls a dice (1–6) on their turn.
Landing on a ladder base moves the player up to its top.
Landing on a snake head moves the player down to its tail.
Players cannot move beyond position 100.
The first player to reach exactly 100 wins.
Surprise tiles trigger special effects determined by a 3-sided dice roll.

Game Structure

Players: Dictionary { 'Red': 0, 'Blue': 0, ... }
Snakes: Dictionary {25:6, 44:23, 65:34, 76:28, 99:56}
Ladders: Dictionary {8:43, 26:39, 38:55, 47:81, 66:92}
Surprise Tiles: List of randomly generated tile positions
Winner: String that stores the name of the winning player

Code Organization

snakes-and-ladders
main.py
README.md
optional helper code documents
The primary logic lives in main.py, organized into reusable functions for clean structure and readability.

Functions Summary

initialise_game(): Sets up the game dictionary with players, snakes, ladders, and starting positions.
get_num_players(): Prompts the user for the number of players (1–4).
play_game(game): Runs an automated game loop until a player wins and returns the winner’s name.
pick_winner(players): Checks if any player’s position equals 100 and returns their name.
turn_by_turn_gameplay(): Enables manual gameplay mode where users input commands like “roll” or “quit”.
generate_surprises(): Randomly generates a list of power tile positions.
special_roll(): Rolls a special 3-sided dice returning 0, 1, or 2 to determine surprise effects.

Power Tiles and Surprises
When a player lands on a surprise tile, they roll a special 3-sided dice. The result determines a unique effect:
Roll 0: The current player rolls again immediately.
Roll 1: The next player loses their next turn.
Roll 2: All other players move back 5 tiles (not below 0).

Priority Rule:
Snakes and ladders take precedence over surprise rolls.
If a player moves via a snake or ladder and lands on a surprise tile afterward, the surprise effect occurs after the snake or ladder movement.

Example Gameplay

Enter number of players (1-4): 2
Player Red is in position 0
Player Blue is in position 0

Player Red rolls a 4
Player Red is in position 4

Player Blue rolls a 6
Player Blue climbed a ladder and is now in position 39

Player Red rolls a 5
Player Red stepped on a snake and is now in position 6

Player Blue has reached 100 and is the winner

How to Run:

Clone this repository:
git clone https://github.com/yourusername/snakes-and-ladders.git
Navigate into the folder:
cd snakes-and-ladders
Run the main script:
python main.py
Follow the on-screen prompts to play manually or view the automatic game simulation.

Final Note

This project showcases a complete progression from basic Python programming to modular and functional design principles.
It is a great way to learn loops, conditionals, lists, dictionaries, user input, and function-driven programming while creating a fun, interactive game.
