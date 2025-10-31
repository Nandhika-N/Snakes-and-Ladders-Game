from diceroll import roll_the_dice
from typing import Tuple

def initialise_game() -> Tuple[list, list, list, list, list, list]:
    # List the possible players
    players = ["Red", "Blue", "Green", "White"]
    # All players will start on position 0
    positions = [0] * len(players)

    # Initialise the snakes and ladders
    # Snake Head Positions
    snake_heads = [25, 44, 65, 76, 99]

    # Snake Tail Positions
    snake_tails = [6, 23, 34, 28, 56]

    # Ladder Base Positions
    ladder_bases = [8, 26, 38, 47, 66]

    # Ladder Tops Positions
    ladder_tops = [43, 39, 55, 81, 92]

    return players, positions, snake_heads, snake_tails, ladder_bases, ladder_tops

def get_num_players() -> int:
    # User can input number of players
    num_players_st = input("Enter the number of players(1-4): ")

    # Player must only input numbers between 1-4 to continue
    while num_players_st not in {"1", "2", "3", "4"}:
        print('Sorry mate, that is an invalid number. Try again: ')
        num_players_st = (input("Enter the number of players(1-4 INTEGERS ONLY): "))

    # Converts input to an integer
    num_players = int(num_players_st)
    return num_players

def play_game(players, positions, snake_heads, snake_tails, ladder_bases, ladder_tops) -> list:
    # Commence the game
    winner = None
    while not winner:
        # Roll the dice for each player and update their position
        for i in range(len(players)):
            diceroll = roll_the_dice()
            # Only add the diceroll if the player does not exceed 100
            if positions[i] + diceroll <= 100:
                positions[i] += diceroll
                print(f'{players[i]} rolled a {diceroll} and is now on position {positions[i]}')
            # Let players know that they rolled a number that adds to above 100.
            elif positions[i] + diceroll > 100:
                print(
                    f'{players[i]} rolled a {diceroll} which is outside the board and cannot move. Good luck for the next round Player {players[i]}!')
            # Check if players are either on a snake head or ladder base
            if positions[i] in snake_heads:
                sn_index = snake_heads.index(positions[i])
                positions[i] = snake_tails[sn_index]
                print(f'Player {players[i]} stepped on a snake and is now on position {positions[i]}')
            if positions[i] in ladder_bases:
                la_index = ladder_bases.index(positions[i])
                positions[i] = ladder_tops[la_index]
                print(f'Player {players[i]} climbed a ladder and is now on position {positions[i]}')
            # Check to see if there is a winner
            if positions[i] == 100:
                winner = players[i]
                combined_position_player = dict(zip(players, positions))
                print(f'Final positions of players {combined_position_player}')
                return positions

        # Combine players and positions into one dictionary that can be printed to show positions of each player
        combined_position_player = dict(zip(players, positions))
        # Print the current positions of the players after each round
        print(f'Updated positions of players {combined_position_player}')

def pick_winner(positions):
    for i in range(len(positions)):
        # Check if player is on tile 100
        if positions[i] == 100:
            # Identifies the player than has won!
            return i
    # The -1 indicates that there is no winner
    return -1

def main():
    players, positions, snake_heads, snake_tails, ladder_bases, ladder_tops = initialise_game()
    # Get the number of players
    num_players = get_num_players()
    # Add the players to the game depending on the user input
    players = players[:num_players]
    positions = positions[:num_players]

    # Print the list of the players to ensure we have the correct set of players
    print(f'These are the {num_players} competitors you have chosen: {players}')
    print(f'All players start at position 0!')

    final_positions = play_game(players, positions, snake_heads, snake_tails, ladder_bases, ladder_tops)
    # Assign winner name using pick_winner function.
    winner = pick_winner(final_positions)
    print(f"The winner is player {players[winner]}!")


if __name__ == '__main__':
    main()