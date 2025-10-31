
from diceroll import roll_the_dice

# Player 1 Name
p1_name = "Red"

# Player 1 Position
p1_position = 0

# Player 2 Name
p2_name = "Blue"

# Player 2 Position
p2_position = 0

# Snake Head Positions
snake_heads = [12,36,50,76,92]

# Snake Tail Positions
snake_tails = [6,16,27,55,89]

# Ladder Base Positions
ladder_bases = [4,14,38,53,80]

# Ladder Tops Positions
ladder_tops = [15,25,60,71,95]

# Roll the dice for the first player
diceroll = roll_the_dice()

# Write the logic to move the first player
if p1_position + diceroll <= 100:
    p1_position += diceroll

# Roll the dice for the second player
diceroll = roll_the_dice()

# Write the logic to move the second player
if p2_position + diceroll <= 100:
    p2_position += diceroll

# Print the position of the first player

print(f'Player {p1_name} is in the position {p1_position}')

# Print the position of the second player

print(f'Player {p2_name} is in the position {p2_position}')
