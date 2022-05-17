import random

board = {
    'top_left': ' ',
    'top_mid': ' ',
    'top_right': ' ',
    'mid_left': ' ',
    'mid_mid': ' ',
    'mid_right': ' ',
    'bot_left': ' ',
    'bot_mid': ' ',
    'bot_right': ' ',
}


def board_frame():
    print(f'{board["top_left"]}|{board["top_mid"]}|{board["top_right"]}')
    print('_____')
    print(f'{board["mid_left"]}|{board["mid_mid"]}|{board["mid_right"]}')
    print('_____')
    print(f'{board["bot_left"]}|{board["bot_mid"]}|{board["bot_right"]}')


player_name = input('Enter your Username: ')
print('Welcome to the most buggy tic tac toe game '.upper())

computer_moves = []
for keys in board.keys():
    computer_moves.append(keys)
print(f"here is a list of moves to navigate the board {computer_moves}".title())

board_frame()
game_over = False
taken = []

#  dear future me, forgive me for writing such a long code for a simple project.
#  I can't begin to explain what I was thinking
#  when I wrote this horrific piece of shitty code... but it worked so that's a plus.
while not game_over:
    turn = 'x'
    userinput = input(f"Its your turn. You're {turn}. Where do you want to serve: ").lower()
    board[userinput] = turn
    taken.append(userinput)
    board_frame()
    if board['top_left'] == turn and board['top_mid'] == turn and board['top_right'] == turn:
        """
        conditions for user to win
        """
        print(f"Player {player_name} is the winner")
        game_over = True
    elif board['mid_left'] == turn and board['mid_mid'] == turn and board['mid_right'] == turn:
        print(f"Player {player_name} is the winner")
        game_over = True
    elif board['bot_left'] == turn and board['bot_mid'] == turn and board['bot_right'] == turn:
        print(f"Player {player_name} is the winner")
        game_over = True
    elif board['top_left'] == turn and board['mid_left'] == turn and board['bot_left'] == turn:
        print(f"Player {player_name} is the winner")
        game_over = True
    elif board['mid_mid'] == turn and board['top_mid'] == turn and board['bot_mid'] == turn:
        print(f"Player {player_name} is the winner")
        game_over = True
    elif board['mid_right'] == turn and board['top_right'] == turn and board['bot_right'] == turn:
        print(f"Player {player_name} is the winner")
        game_over = True
    elif board['top_left'] == turn and board['mid_mid'] == turn and board['bot_right'] == turn:
        print(f"Player {player_name} is the winner")
        game_over = True
    elif board['bot_left'] == turn and board['mid_mid'] == turn and board['top_right'] == turn:
        print(f"Player {player_name} is the winner")
        game_over = True
    else:
        if turn == 'x':
            turn = 'o'
            available_moves = []
            for move in computer_moves:
                if move not in taken:
                    available_moves.append(move)
            print("******************* Computer's turn ***************************")
            comp_pick = random.choice(available_moves)
            board[comp_pick] = turn
            taken.append(comp_pick)
            board_frame()
            if board['top_left'] == turn and board['top_mid'] == turn and board['top_right'] == turn:
                """
                conditions for computer to win
                """
                print(f"The computer wins")
                game_over = True
            elif board['mid_left'] == turn and board['mid_mid'] == turn and board['mid_right'] == turn:
                print(f"The computer wins")
                game_over = True
            elif board['bot_left'] == turn and board['bot_mid'] == turn and board['bot_right'] == turn:
                print(f"The computer wins")
                game_over = True
            elif board['top_left'] == turn and board['mid_left'] == turn and board['bot_left'] == turn:
                print(f"The computer wins")
                game_over = True
            elif board['mid_mid'] == turn and board['top_mid'] == turn and board['bot_mid'] == turn:
                print(f"The computer wins")
                game_over = True
            elif board['mid_right'] == turn and board['top_right'] == turn and board['bot_right'] == turn:
                print(f"The computer wins")
                game_over = True
            elif board['top_left'] == turn and board['mid_mid'] == turn and board['bot_right'] == turn:
                print(f"The computer wins")
                game_over = True
            elif board['bot_left'] == turn and board['mid_mid'] == turn and board['top_right'] == turn:
                print(f"The computer wins")
                game_over = True
        else:
            turn = 'x'
#  for developers who might review this code. I am very sorry for this atrocity I wrote. Feel
#  free to leave corrections.
