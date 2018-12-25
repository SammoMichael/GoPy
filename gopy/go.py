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
game = board_map
players = ['player1', 'player2']
turns = [0, 1]
current_turn = 1

def on_edge(x, y):
    if x == 0 and (y != 0 or y != board_size - 1):
        return 'w'
    elif x == board_size - 1 and (y != board_size - 1 or y != 0):
        return 'e'
    elif y == 0 and (x != 0 or x != board_size - 1):
        return 'n'
    elif y == board_size - 1 and (x != board_size - 1 or x != 0):
        return 's'
    return False

def on_corner(x, y):
    if (x == 0 and y == 0):
        return 'nw' 
    elif (x == board_size - 1 and y == board_size - 1 ):
        return 'se'  
    elif (x == board_size - 1 and y == 0): 
        return 'ne'
    elif (y == board_size - 1 and x == 0):
        return 'sw'
    return False

def on_board(x, y):
    if (x >= 0 and x <= board_size - 1) and (y >= 0 and y <= board_size - 1):
        return True 
    return False 

def check_liberties(x, y):
    global game
    # if on_edge(x, y):
    #     print(on_edge(x, y))
    # if on_corner(x, y):
    #     print(on_corner(x, y))
    # if game[x+1][y] == 2 and game[x][y+1] and game[x][y-1] == 2 and game[x-1][y] == 2:
    # game[x][y] = 0
    if game[x][y] == 1:
        if game[x+1][y] == 2 and game[x][y+1] and game[x][y-1] == 2 and game[x-1][y] == 2:
            game[x][y] = 0
    if game[x][y] == 2:
        if game[x+1][y] == 2 and game[x][y+1] and game[x][y-1] == 2 and game[x-1][y] == 1:
            game[x][y] = 0
    

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

white_groups = []
black_groups = []

# def check_adjacency(x,y):
#     if [x, y] in white_groups or [x, y] in black_groups:
#         return 
#     # print(black_groups)
#     # print(white_groups)
#     if game[x][y] == 2:
#             # white_groups.append()
#             if game[x+1][y] == 2:
#                 if [x+1][y] not in white_groups:
#                     white_groups.append([x+1, y])
#                 elif [x][y] not in white_groups:
#                     white_groups.append([x, y])
#                 # check_adjacency(x+1, y)
#                     # black_groups.append([x, y], [x+1, y])
#             elif game[x-1][y] == 2:
#                 if [x-1][y] not in white_groups:
#                     white_groups.append([x-1, y])
#                 elif [x][y] not in white_groups:
#                     white_groups.append([x, y])

#                 # black_groups.append([x, y], [x-1, y])

#             elif game[x][y-1] == 2:
#                 if [x][y-1] not in white_groups:
#                     white_groups.append([x, y-1])
#                 elif [x][y] not in white_groups:
#                     white_groups.append([x, y])

#                 # black_groups.append([x, y], [x, y-1])

#             elif game[x][y+1] == 2:
#                 if [x][y+1] not in white_groups:
#                     white_groups.append([x, y+1])

#                 # black_groups.append([x, y], [x, y+1])
#     if game[x][y] == 1:
#             if game[x+1][y] == 1:
#                 print('adjacent')

#                 # black_groups.append([x, y], [x+1, y])
#             elif game[x-1][y] == 1:
#                 print('adjacent')

#                 # black_groups.append([x, y], [x-1, y])

#             elif game[x][y-1] == 1:
#                 print('adjacent')

#                 # black_groups.append([x, y], [x, y-1])

#             elif game[x][y+1] == 1:
#                 print('adjacent')

#                 # black_groups.append([x, y], [x, y+1])
         

def update_board(board_map = board_map, player = 0, row = 0, col = 0):
    try: 
        if board_map is not None:
            # print(chr(27) + "[2J")
            prGreen('   0  1  2  3  4  5  6  7  8')
            board_map[row][col] = player
            for count, row in enumerate(board_map):
                for count2, stone in enumerate(row): 
                    # pdb.set_trace()
                    check_liberties(count, count2)
                    # check_adjacency(count2, count)
                prPurple(row)
                prGreen(count)
                # print(board_map)
                # pdb.set_trace()
            return board_map
    except IndexError as e: print(e)
    except: print('sorry, something went awry')

def get_move():
    try:
        move = input("move")
        move_y = (int(move[0]))
        move_x = (int(move[1]))
        if occupied_space(move_x, move_y):
            raise Exception
        if on_board(move_x, move_y) == False:
            raise Exception
        # pdb.set_trace()
        print([move_x, move_y])           
        return [move_x, move_y]
    except Exception as e: print("invalid move", e)
    # get_move()

def game_loop(board_map):
    try:
        update_board()
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
