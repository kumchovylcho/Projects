import random


def rock_paper_scissors():
    possible_words = "paper", "rock", "scissors"
    player_choice = input("Choose [paper], [rock] or [scissors] to fight for who draws first:\n").lower()
    random_computer_roll = computer_throw_dice_rock_paper_scissors()
    draw = False
    if player_choice == "paper":
        if random_computer_roll == 2:
            print(f"Computer wins with {possible_words[random_computer_roll]}.\n{possible_words[random_computer_roll]} > {player_choice}")

        elif random_computer_roll == 1:
            print(f"You win.You are the first to draw on the board.\n{player_choice} > {possible_words[random_computer_roll]}")

        elif random_computer_roll == 0:
            print(f"Draw!   {player_choice} = {possible_words[random_computer_roll]}")
            draw = True
    elif player_choice == "rock":
        if random_computer_roll == 2:
            print(f"You win.You are the first to draw on the board.\n{player_choice} > {possible_words[random_computer_roll]}")

        elif random_computer_roll == 1:
            print(f"Draw!   {player_choice} = {possible_words[random_computer_roll]}")
            draw = True
        elif random_computer_roll == 0:
            print(f"Computer wins with {possible_words[random_computer_roll]}.\n{possible_words[random_computer_roll]} > {player_choice}")

    elif player_choice == "scissors":
        if random_computer_roll == 2:
            print(f"Draw!   {player_choice} = {possible_words[random_computer_roll]}")
            draw = True
        elif random_computer_roll == 1:
            print(f"Computer wins with {possible_words[random_computer_roll]}.\n{possible_words[random_computer_roll]} > {player_choice}")

        elif random_computer_roll == 0:
            print(f"You win.You are the first to draw on board.\n{player_choice} > {possible_words[random_computer_roll]}")

    else:
        rock_paper_scissors()
    if draw:
        rock_paper_scissors()


def computer_throw_dice_rock_paper_scissors():
    return random.randint(0, 2)


rock_paper_scissors()