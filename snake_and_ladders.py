import random
obstacles = {
    'ladders':
        {1: 38,
         4: 14,
         9: 31,
         21: 42,
         28: 84,
         51: 67,
         72: 91,
         80: 99},
    'snakes':
        {17: 7,
         54: 34,
         62: 19,
         64: 60,
         87: 36,
         93: 73,
         94: 75,
         98: 79}
}
player_field = []
computer_field = []
for set_letters in range(1, 101):
    if set_letters in obstacles['ladders']:
        player_field.append('l'), computer_field.append('l')
    elif set_letters in obstacles['snakes']:
        player_field.append('s'), computer_field.append('s')
    else:
        player_field.append('_'), computer_field.append('_')

player_name = ''
player_position = 0
computer_position = 0

print("Welcome to my snake and ladders game!\n\nBest of luck!")


def player_nickname():
    global player_name
    username = input("Enter your nickname: ")
    while len(username) < 1:
        username = input("Enter your nickname: ")
    player_name = username[0].upper()
    print(f"{player_name} {''.join(player_field)}\n\nC {''.join(computer_field)}")
    user_move()


def user_move():
    global player_position
    input("\nPress Enter or any key to throw!\n")
    current_dice = dice_roller()
    if player_position + current_dice in obstacles['ladders'] and player_position < 100:
        player_position = obstacles['ladders'][player_position + current_dice]

    elif player_position + current_dice in obstacles['snakes'] and player_position < 100:
        player_position = obstacles['snakes'][player_position + current_dice]

    elif player_position + current_dice not in obstacles['ladders'] \
            and player_position + current_dice not in obstacles['snakes'] \
            and player_position + current_dice <= 100:
        player_position += current_dice
    show_positions()
    if player_position == 100:
        print(f"\n\n{player_name} wins!")
        show_positions()
        new_game()
    elif player_position < 100:
        computer_move()


def computer_move():
    global computer_position
    current_dice = dice_roller()
    if computer_position + current_dice in obstacles['ladders'] and computer_position < 100:
        computer_position = obstacles['ladders'][computer_position + current_dice]

    elif computer_position + current_dice in obstacles['snakes'] and computer_position < 100:
        computer_position = obstacles['snakes'][computer_position + current_dice]

    elif computer_position + current_dice not in obstacles['ladders'] \
            and computer_position + current_dice not in obstacles['snakes'] \
            and computer_position + current_dice <= 100:
        computer_position += current_dice
    if computer_position == 100:
        print("\n\nComputer wins!")
        show_positions()
        new_game()
    elif computer_position < 100:
        user_move()


def dice_roller():
    return random.randint(1, 6)


def show_positions():
    player_field.insert(player_position, player_name), computer_field.insert(computer_position, 'C')
    player_tracker = f"{player_field.index(player_name) * ' '}^{(100 - player_field.index(player_name)) * ' '}"
    computer_tracker = f"{computer_field.index('C') * ' '}^{(100 - computer_field.index('C')) * ' '}"
    print(f"{''.join(player_field)}\n{player_tracker}\n{''.join(computer_field)}\n{computer_tracker}")
    player_field.remove(player_name), computer_field.remove('C')


def new_game():
    global player_position, computer_position, player_name
    new_game_question = input("\nDo you want to start a new game? [Y] / [N] : ")
    while new_game_question != 'Y' or new_game_question != 'N':
        if new_game_question == 'Y':
            player_position, computer_position = 0, 0
            change_username = input("\nDo you want to change your nickname? [Y] / [N] : ")
            while change_username != 'Y' or change_username != 'N':
                if change_username == 'Y':
                    player_name = ''
                    player_nickname()
                elif change_username == 'N':
                    user_move()
                change_username = input("\nDo you want to change your nickname? [Y] / [N] : ")
        elif new_game_question == 'N':
            print("\nThank you for playing my game!")
            exit()
        new_game_question = input("\nDo you want to start a new game? [Y] / [N] : ")


player_nickname()
