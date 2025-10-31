from diceroll import roll_the_dice, special_roll
from helpers import generate_surprises


def initialise_game() -> dict:
    # Create empty dictionary called game
    game = {}

    # Add the possible players to dictionary
    game["players"] = {"Red": 0, "Blue": 0, "Green": 0, "White": 0}
    # Add the snake heads as keys and snake tails as values to dictionary
    game["snakes"] = {'25': 6, '44': 23, '65': 34, '76': 28, '99': 56}
    # Add the ladder bases as keys and ladder tops as values to dictionary
    game["ladders"] = {'8': 43, '26': 39, '38': 55, '47': 81, '66': 92}
    return game


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


def rolling_dice(game, player):
    diceroll = roll_the_dice()
    new_position = game["players"][player] + diceroll
    # Only add the diceroll if the player does not exceed 100
    if new_position == 100:
        game["players"][player] = 100
        print(f'{player} rolled a {diceroll} and reached 100')
        print(f'Positions: {game["players"]}')
        return game["players"][player]
    elif new_position < 100:
        game["players"][player] = new_position
        print(f'{player} rolled a {diceroll} and is now on position {game["players"][player]}')
    # Let players know that they rolled a number that adds to above 100.
    else:
        print(
            f'{player} rolled a {diceroll} which is outside the board and cannot move. Good luck for the next round Player {player}!')
    return game["players"][player]


def snakes_ladders(game, player):
    while str(game["players"][player]) in game["snakes"] or str(game["players"][player]) in game["ladders"]:
        # Check if players are either on a snake head or ladder base
        if str(game["players"][player]) in game["snakes"]:
            game["players"][player] = int(game["snakes"][str(game["players"][player])])
            print(f'Player {player} stepped on a snake and is now on position {game["players"][player]}')

        if str(game["players"][player]) in game["ladders"]:
            game["players"][player] = int(game["ladders"][str(game["players"][player])])
            print(f'Player {player} climbed a ladder and is now on position {game["players"][player]}')

    if str(game["players"][player]) in game["surprise_tiles"]:
        return power_tiles_auto(game, player, False)

    return game["players"][player]


def add_chosen_players(game, num_players):
    # New dictionary which will have the selected number of players
    chosen_players = {}
    # Add to chosen_players dictionary using user input stored as num_players
    count = 0
    for key, value in game["players"].items():
        if count >= num_players:
            break
        chosen_players[key] = value
        count += 1
    print(f'Starting positions:{chosen_players}')
    game["players"].clear()
    game["players"].update(chosen_players)
    return game["players"]


def power_tiles_auto(game, player, skip_turn):
    # Check if players are on a special tile
    if game["players"][player] not in game["surprise_tiles"]:
        return
    special = special_roll()
    if special == 0:
        print(f'{player} is now on a power tile and rolled a 0! They get to roll again!')
        if game["players"][player] == 100:
            print(f'{player} has reached 100!')
            return
        rolling_dice(game, player)
        snakes_ladders(game, player)
        return power_tiles_auto(game, player, skip_turn)

    elif special == 1:
        next_player = get_next_player(game, player)
        game["skip_turns"][next_player] = True
        print(f'{player} is now on a power tile and rolled a 1! Player {next_player} loses a turn!')

    elif special == 2:
        print(f'{player} is on a power tile and rolled a 2. All other players will go back by 5 tiles')
        game["move_back_5"] = True
    return skip_turn


def get_next_player(game, current_player):
    players = list(game["players"].keys())
    current_index = players.index(current_player)
    next_index = (current_index + 1) % len(players)  # Loop back if last player
    return players[next_index]


def play_game(game: dict) -> str:
    game["surprise_tiles"] = generate_surprises()
    skip_turn = False
    game["skip_turns"] = {player: False for player in game["players"]}
    game["move_back_5"] = False
    winner = None
    while not winner:

        for player in game["players"]:
            if game["skip_turns"][player]:
                print(f'{player} must skip their turn!')
                game["skip_turns"][player] = False
                continue

            rolling_dice(game, player)
            snakes_ladders(game, player)
            winner = pick_winner(game["players"])
            if winner:
                return winner
            skip_turn = power_tiles_auto(game, player, skip_turn)
            if game["move_back_5"]:
                print("All other players must move back 5 tiles")
                for other_players in game["players"]:
                    if other_players != player:
                        if game["players"][other_players] <= 5:
                            game["players"][other_players] = 0
                        else:
                            game["players"][other_players] -= 5
                game["move_back_5"] = False
        # Print the current positions of the players
        print(f'Positions: {game["players"]}')


def pick_winner(players: dict) -> str:
    for player, position in players.items():
        if position == 100:
            # Identifies the player than has won!
            return player
    # The None indicates that there is no winner
    return None


def power_tiles_turn(game, player, skip_turn):
    # Check if players are on a special tile

    if game["players"][player] not in game["surprise_tiles"]:
        return
    special = special_roll()

    if special == 0:
        print(f'{player} is now on a power tile and rolled a 0! They get to roll again!')
        ask = input(f"{player} please type 'roll' to roll the dice again!")
        if ask == 'roll':
            rolling_dice(game, player)
            snakes_ladders(game, player)
            return power_tiles_turn(game, player, skip_turn)
        else:
            print("Input was not recognised. Try typing 'roll' again")

    elif special == 1:
        next_player = get_next_player(game, player)
        game["skip_turns"][next_player] = True
        print(f'{player} is now on a power tile and rolled a 1! Player {next_player} loses a turn!')
        return True

    elif special == 2:
        print(f'{player} is on a power tile and rolled a 2. All other players will go back by 5 tiles')
        for other_players in game["players"]:
            if other_players != player:
                if game["players"][other_players] <= 5:
                    game["players"][other_players] = 0
                else:
                    game["players"][other_players] -= 5
    return skip_turn


def turn_by_turn_gameplay():
    print("You have selected the Manual Game Mode")
    # Select the two players
    game = initialise_game()
    add_chosen = add_chosen_players(game, 2)
    game["surprise_tiles"] = generate_surprises()
    players = list(game["players"].keys())
    winner = None
    skip_turn = False
    game["skip_turns"] = {player: False for player in game["players"]}

    while not winner:
        for player in players:
            if skip_turn:
                print(f'{player} skips this turn')
                skip_turn = False
                continue

            while True:
                verb = input(
                    f"{player} can you type 'roll' (in lowercase) if you would like to roll the dice or 'quit' to end the game ")
                if verb in {'roll', 'quit'}:
                    break
                print(f"Try again")

            if verb == "quit":
                print(f'{player} quit this game')
                return

            rolling_dice(game, player)
            snakes_ladders(game, player)
            skip_turn = power_tiles_turn(game, player, skip_turn)

            # Check to see if there is a winner
            winner = pick_winner(game["players"])
            if winner:
                print(f'The winner is {winner}')
                return

            # Print the current positions of the players
            print(f'Positions: {game["players"]}')


def game_choice():
    # User can input and choose to play with manual two-player game or let the computer play by itself.
    player_gamechoice = input(
        f"Choose either 'auto' (computer plays by itself - up to 4 players) or 'manual'(you can play the game manually - 2 players) ")
    return player_gamechoice


def main():
    while True:
        # This function will ask the user to choose the type of game they want to play
        player_gamechoice = game_choice()

        # Depending on user choice, call auto functions or manual functions.

        # Auto game
        if player_gamechoice == 'auto':
            print("You have selected the Auto Game Mode")
            # Initialises the 'game' dictionary
            game = initialise_game()

            # Uses the user input to return the number of players
            num_players = get_num_players()

            # Calls a function that will add the chosen number of players to game dictionary
            add_chosen = add_chosen_players(game, num_players)

            # Start the game
            winner = play_game(game)
            if winner:  # When the pick_winner() function returns a players name and passes it to play_game() the winner can be printed as it is no longer returns 'None'.
                print(f"The winner is {winner}!")
            break

        # Turn by turn game
        elif player_gamechoice == 'manual':
            turn_by_turn_gameplay()
            break

        # Else statement ensures the player will have to re-type input if they type anything other than "auto" or "manual".
        else:
            print("Try again")


if __name__ == '__main__':
    main()
