
from diceroll import roll_the_dice

# Initialise the players
# Player 1 Name
p1_name = "Red"

# Player 1 Position
p1_position = 0

# Player 2 Name
p2_name = "Blue"

# Player 2 Position
p2_position = 0

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
while p1_position < 100 and p2_position < 100:
    # Roll the dice for the red player
    diceroll = roll_the_dice()

    # Write the logic to move the red player
    # Check to see if the resultant position is within the board
    if p1_position + diceroll <= 100:
        p1_position += diceroll

        # Check if player 1 is either on a snake head or ladder Base
    for i in range(len(snake_heads)):
        if p1_position == snake_heads[i]:
            p1_position = snake_tails[i]
            print(f'Player {p1_name} stepped on a snake and is now in position {p1_position}')
    for i in range(len(ladder_bases)):
        if p1_position == ladder_bases[i]:
            p1_position = ladder_tops[i]
            print(f'Player {p1_name} climbed a ladder and is now in position {p1_position}')

    # Roll the dice for the blue player
    # Check to see if red player has already won
    if p1_position != 100:
        diceroll = roll_the_dice()
    else:
        break

    # Write the logic to move the blue player
    if p2_position + diceroll <= 100:
        p2_position += diceroll

        # Check if player 2 is either on a snake head or ladder Base
    for i in range(len(snake_heads)):
        if p2_position == snake_heads[i]:
            p2_position = snake_tails[i]
            print(f'Player {p2_name} stepped on a snake and is now in position {p2_position}')
    for i in range(len(ladder_bases)):
        if p2_position == ladder_bases[i]:
            p2_position = ladder_tops[i]
            print(f'Player {p2_name} stepped on a snake and is now in position {p2_position}')

    # Print the current positions of the players 
    print(f'Player {p1_name} is in the position {p1_position} \n Player {p2_name} is in the position {p2_position}')
    if p1_position == 100 or p2_position == 100:
        break

# Check to see if there is a winner
if p1_position == 100:
    winner = p1_name
elif p2_position == 100:
    winner = p2_name

# Announce the winner
print(f'Player {winner} has reached 100 and is the winner!')
