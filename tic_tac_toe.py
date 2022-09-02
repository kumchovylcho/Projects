import random
game_board = ["-", "-", "-",
              "-", "-", "-",
              "-", "-", "-"]

player_marker = "O"
tic_tac_toe_winner = None


def print_board(game_board):
    print(f"{game_board[0]} | {game_board[1]} | {game_board[2]}")
    print("---------")
    print(f"{game_board[3]} | {game_board[4]} | {game_board[5]}")
    print("---------")
    print(f"{game_board[6]} | {game_board[7]} | {game_board[8]}")


def player_move(game_board):
    global player_marker
    allowed_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    player_input = input("Enter a number 1-9: ")
    if player_input in allowed_numbers:
        player_input = int(player_input)
        if 1 <= player_input <= 9 and game_board[player_input - 1] == "-":
            game_board[player_input - 1] = player_marker

        elif 1 <= player_input <= 9 and game_board[player_input - 1] != "-":
            print("\nSpot is already marked.")
            player_move(game_board)

    elif player_input not in allowed_numbers:
        player_move(game_board)


def computer_move(game_board):
    while player_marker == "X":
        position = random.randint(0, 8)
        if game_board[position] == "-":
            game_board[position] = "X"
            switch_player()


def switch_player():
    global player_marker
    if player_marker == "X":
        player_marker = "O"
    elif player_marker == "O":
        player_marker = "X"


def check_horizontal(game_board):
    global tic_tac_toe_winner
    if game_board[0] == game_board[1] == game_board[2] and game_board[0] != "-":
        tic_tac_toe_winner = game_board[0]
        return True
    elif game_board[3] == game_board[4] == game_board[5] and game_board[3] != "-":
        tic_tac_toe_winner = game_board[3]
        return True
    elif game_board[6] == game_board[7] == game_board[8] and game_board[6] != "-":
        tic_tac_toe_winner = game_board[6]
        return True


def check_vertical(game_board):
    global tic_tac_toe_winner
    if game_board[0] == game_board[3] == game_board[6] and game_board[0] != "-":
        tic_tac_toe_winner = game_board[0]
        return True
    elif game_board[1] == game_board[4] == game_board[7] and game_board[1] != "-":
        tic_tac_toe_winner = game_board[1]
        return True
    elif game_board[2] == game_board[5] == game_board[8] and game_board[2] != "-":
        tic_tac_toe_winner = game_board[2]
        return True


def check_diagonal(game_board):
    global tic_tac_toe_winner
    if game_board[0] == game_board[4] == game_board[8] and game_board[0] != "-":
        tic_tac_toe_winner = game_board[0]
        return True
    elif game_board[2] == game_board[4] == game_board[6] and game_board[2] != "-":
        tic_tac_toe_winner = game_board[2]
        return True


def check_for_tie(game_board):
    global game_is_played
    if "-" not in game_board:
        print_board(game_board)
        print("Draw!")
        game_is_played = False


def check_winner(game_board):
    global game_is_played
    if check_diagonal(game_board) or check_horizontal(game_board) or check_vertical(game_board):
        print(f"\n\nThe winner is {tic_tac_toe_winner}")
        game_is_played = False


game_is_played = True
while game_is_played:
    print_board(game_board)
    player_move(game_board)
    check_winner(game_board)
    check_for_tie(game_board)
    switch_player()

    computer_move(game_board)
    check_winner(game_board)
    check_for_tie(game_board)

print()
print_board(game_board)
