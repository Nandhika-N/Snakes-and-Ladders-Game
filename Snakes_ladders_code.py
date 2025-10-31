
from diceroll import roll_the_dice

# List the possible players
player_colours = ["Red", "Blue", "Green", "White"]

# Define an empty list for players (elements will be added depending on user input)
players = []

# User can input number of players
num_players_any_type = input("Enter the number of players(1-4): ")

# Player must only input numbers between 1-4 to continue
while num_players_any_type != "1" and num_players_any_type != '2' and num_players_any_type != '3' and num_players_any_type != '4':
    print('Sorry mate, that is an invalid number. Try again: ')
    num_players_any_type = (input("Enter the number of players(1-4 INTEGERS ONLY): "))

# Converts input to an integer
num_players = int(num_players_any_type)

# Initialize players---

# Add the players depending on the user input
players = player_colours[:num_players]

# Print the list of the players to ensure we have the correct set of players
print(f'These are the {num_players} competitors you have chosen: {players}')

# Define a new dictionary that will show the positions of each player
positions = []

# All players will start on position 0
for player in players:
    positions.append(0)

# Initialise the snakes and ladders
# Snake Head Positions
snake_heads = [25, 44, 65, 76, 99]

# Snake Tail Positions
snake_tails = [6, 23, 34, 28, 56]

# Ladder Base Positions
ladder_bases = [8, 26, 38, 47, 66]

# Ladder Tops Positions
ladder_tops = [43, 39, 55, 81, 92]

# Commence the game
winner = None
while not winner:
    # Roll the dice for each player and update their position
    for player in players:
        current_player_index = players.index(player)
        print(current_player_index)
        diceroll = roll_the_dice()
        if positions[current_player_index] + diceroll <= 100:
            positions[current_player_index] += diceroll
            print(f'{player} rolled a {diceroll} and is now on position {positions[current_player_index]}')

            # Check if players are either on a snake head or ladder base
            for i in range(len(snake_heads)):
                if positions[current_player_index] == snake_heads[i]:
                    positions[current_player_index] = snake_tails[i]
                    print(
                        f'Player {player} stepped on a snake and is now in position {positions[current_player_index]}')
            for i in range(len(ladder_bases)):
                if positions[current_player_index] == ladder_bases[i]:
                    positions[current_player_index] = ladder_tops[i]
                    print(f'Player {player} climbed a ladder and is now in position {positions[current_player_index]}')
            # Check to see if there is a winner
            if positions[current_player_index] == 100:
                winner = player
                break

    # Print the current positions of the players
    print(positions)

# Announce the winner
print(f'Player {winner} has reached 100 and is the winner!')