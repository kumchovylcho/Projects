import random        # IT PLAYS BY ITSELF WITH RED AND BLUE PLAYERS
                     # THIS IS NOT FULL VERSION OF THE GAME
red_pawn = 1
blue_pawn = 1

red_position = 0
blue_position = 0

max_dice_6_count = 1   # 2 times

counter_of_6_in_a_roll = 0


def dice():
    return random.randint(1, 6)


def blue_player_rolls_in_base():
    global blue_pawn
    roll = dice()
    if roll != 6:
        print(f"Blue player throws {roll} from base.")
        if red_pawn > 0:
            red_player_rolls_in_base()
        elif red_pawn == 0:
            red_player_in_game()
    elif roll == 6:
        print(f"Blue player got his pawn out of base with roll {roll}")
        blue_pawn -= 1
        blue_player_in_game()


def red_player_rolls_in_base():
    global red_pawn
    roll = dice()
    if roll != 6:
        print(f"Red player throws {roll} from base.")
        if blue_pawn > 0:
            blue_player_rolls_in_base()
        elif blue_pawn == 0:
            blue_player_in_game()
    elif roll == 6:
        print(f"Red player got his pawn out of base with roll {roll}")
        red_pawn -= 1
        red_player_in_game()


def blue_player_in_game():
    global blue_position
    global counter_of_6_in_a_roll
    roll = dice()

    if blue_position + roll > 30:
        print(f"Blue player rolled {roll}")
        print(f"Blue skips turn. Current position {blue_position}/30.")

    elif blue_position + roll <= 30:
        blue_position += roll
        print(f"Blue player has moved with {roll}, current position {blue_position}/30.")
        if blue_position == 30:
            print("Blue player won the game")
            exit()

    if roll == 6:
        counter_of_6_in_a_roll += 1
        blue_player_in_game()
        if counter_of_6_in_a_roll > max_dice_6_count:
            counter_of_6_in_a_roll = 0
    counter_of_6_in_a_roll = 0
    red_pawn_checker()


def red_player_in_game():
    global red_position
    global counter_of_6_in_a_roll
    roll = dice()

    if red_position + roll > 30:
        print(f"Red player rolled {roll}")
        print(f"Red skips turn. Current position {red_position}/30.")

    elif red_position + roll <= 30:
        red_position += roll
        print(f"Red player has moved with {roll}, current position {red_position}/30.")
        if red_position == 30:
            print("Red player won the game")
            exit()

    if roll == 6:
        counter_of_6_in_a_roll += 1
        red_player_in_game()
        if counter_of_6_in_a_roll > max_dice_6_count:
            counter_of_6_in_a_roll = 0
    counter_of_6_in_a_roll = 0
    blue_pawn_checker()


def red_pawn_checker():
    global red_pawn
    if red_pawn == 0:
        red_player_in_game()
    elif red_pawn > 0:
        red_player_rolls_in_base()


def blue_pawn_checker():
    global blue_pawn
    if blue_pawn == 0:
        blue_player_in_game()
    elif blue_pawn > 0:
        blue_player_rolls_in_base()


red_player_rolls_in_base()
