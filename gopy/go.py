import sys
import pdb 
import numpy as np

def prRed(prt): print("\033[91m {}\033[00m" .format(prt))
def prGreen(prt): print("\033[92m {}\033[00m" .format(prt))
def prYellow(prt): print("\033[93m {}\033[00m" .format(prt))
def prLightPurple(prt): print("\033[94m {}\033[00m" .format(prt))
def prPurple(prt): print("\033[95m {}\033[00m" .format(prt))
def prCyan(prt): print("\033[96m {}\033[00m" .format(prt))
def prLightGray(prt): print("\033[97m {}\033[00m" .format(prt))
def prBlack(prt): print("\033[98m {}\033[00m" .format(prt))



board_size = int(input("board size?"))

board_map = np.zeros( (board_size, board_size) )


# board_map = [
#     ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
#     ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
#     ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
#     ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
#     ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
#     ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
#     ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
#     ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
#     ['0', '0', '0', '0', '0', '0', '0', '0', '0']
# ]

# class Board 
#     pass 
    
game = board_map
players = ['player1', 'player2']
turns = [0, 1]
current_turn = 1

def occupied_space(x, y):
    if game[x][y] != 0:
        return True 
    return False 

def current_player_mark():
    return {'player1': '1', 'player2': '2'}.get(current_player())

def current_player_color():
    if current_player() == 1:
        return 'white'
    return 'black'

def current_player():
    global current_turn 
    current_turn += 1
    print(players[(current_turn) % 2])
    return players[(current_turn) % 2]


# def check_valid_move(x, y):
#     return valid_move(x, y)


# def []=:
#     pass

# def check_liberties: 
#     for x in board_map:
#         pass 


# def invalid_move(x, y):
#     return board_map[x][y] == 1 or board_map[x][y] == 2


def update_board(board_map = board_map, player = 0, row = 0, col = 0):
    try: 
        if board_map is not None:
            print(chr(27) + "[2J")
            prGreen('   0  1  2  3  4  5  6  7  8')
            board_map[row][col] = player
            for count, row in enumerate(board_map):
                prPurple(row)
                prGreen(count)
                # print(board_map)
            return board_map
    except IndexError as e: print(e)
    except: print('sorry, something went awry')


def get_move():
    try:
        move = input("move")
        move_x = (int(move[0]))
        move_y = (int(move[1]))
        if occupied_space(move_x, move_y):
            raise Exception
        # pdb.set_trace()
        # invalid = (invalid_move(move_x, move_y))
        # print(invalid)
        # if invalid == True:
        #     raise ValueError() 
        print([move_x, move_y])           
        return [move_x, move_y]
    except Exception as e: print("invalid move", e)
    get_move()


def game_loop(board_map):
    try:
        if board_map is not None:
            game_over = False
            while (game_over != True):
                new_move = get_move()
                if new_move is not None:
                    game = update_board(board_map, current_player_mark(), new_move[0], new_move[1])
            return game
    except TypeError as e: print(e)
    game = update_board(board_map, current_player_mark(),new_move[0], new_move[1])
game_loop(game)
