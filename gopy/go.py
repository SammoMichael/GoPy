
import sys
import pdb 
import numpy as np
import random


    # rest of code
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
last_index = board_size - 1
game = board_map
players = ['player1', 'player2']
turns = [0, 1]
current_turn = 1
white_captured = 0
black_captured = 0




def on_corner(x, y):
    if (x == 0 and y == 0):
        return 'nw' 
    elif (x == last_index and y == last_index ):
        return 'se'  
    elif (x == last_index and y == 0): 
        return 'ne'
    elif (y == last_index and x == 0):
        return 'sw'
    elif x == 0:
        return 'w'
    elif y == 0:
        return 'n'
    elif x == last_index:
        return 'e'
    elif y == last_index:
        return 's'
    return False

def on_board(x, y):
    if (x >= 0 and x <= last_index) and (y >= 0 and y <= last_index):
        return True 
    return False 

def check_liberties(x, y):
    # pdb.set_trace()
    try: 
        global white_captured
        global black_captured
        global game
        if on_corner(x, y) == 's' and game[x][y] == 2:
            if game[x][y-1] == 1 and game[x+1][y] == 1 and game[x-1][y] == 1:
                game[x][y] = 0
                white_captured += 1
                return game[x][y]
        elif on_corner(x, y) == 's' and game[x][y] == 1:
            if game[x][y-1] == 2 and game[x+1][y] == 2 and game[x-1][y] == 2:
                game[x][y] = 0
                black_captured += 1
                return game[x][y]
        elif on_corner(x, y) == 'n' and game[x][y] == 2:
            if game[x][y+1] == 1 and game[x+1][y] == 1 and game[x-1][y] == 1:
                game[x][y] = 0
                white_captured += 1
                return game[x][y]
        elif on_corner(x, y) == 'n' and game[x][y] == 1:
            if game[x][y+1] == 2 and game[x+1][y] == 2 and game[x-1][y] == 2:
                game[x][y] = 0
                black_captured += 1
                return game[x][y]
        elif on_corner(x, y) == 'e' and game[x][y] == 2:
            if game[x-1][y] == 1 and game[x][y-1] == 1 and game[x][y+1] == 1:
                game[x][y] = 0
                white_captured += 1
                return game[x][y]
        elif on_corner(x, y) == 'e' and game[x][y] == 1:
            if game[x-1][y] == 2 and game[x][y-1] == 2 and game[x][y+1] == 2:
                game[x][y] = 0
                black_captured += 1
                return game[x][y]
        elif on_corner(x, y) == 'w' and game[x][y] == 2:
            if game[x+1][y] == 1 and game[x][y-1] == 1 and game[x][y+1] == 1:
                game[x][y] = 0
                white_captured += 1
                return game[x][y]
        elif on_corner(x, y) == 'w' and game[x][y] == 1:
            if game[x+1][y] == 2 and game[x][y-1] == 2 and game[x][y+1] == 2:
                game[x][y] = 0
                black_captured += 1
                return game[x][y]
        elif on_corner(x, y) == 'ne' and game[x][y] == 2:
            if game[x-1][y] == 1 and game[x][y+1] == 1:
                game[x][y] = 0
                white_captured += 1
                return game[x][y]
        elif on_corner(x, y) == 'ne' and game[x][y] == 1:
            if game[x-1][y] == 2 and game[x][y+1] == 2:
                game[x][y] = 0
                black_captured += 1
                return game[x][y]
        elif on_corner(x, y) == 'nw' and game[x][y] == 2:
            if game[x+1][y] == 1 and game[x][y+1] == 1:
                game[x][y] = 0
                white_captured += 1
                return game[x][y]
        elif on_corner(x, y) == 'nw' and game[x][y] == 1:
            if game[x+1][y] == 2 and game[x][y+1] == 2:
                game[x][y] = 0
                black_captured += 1
                return game[x][y]
        elif on_corner(x, y) == 'se' and game[x][y] == 1:
            if game[x-1][y] == 2 and game[x][y-1] == 2:
                game[x][y] = 0
                black_captured += 1
                return game[x][y]
        elif on_corner(x, y) == 'se' and game[x][y] == 2:
            if game[x-1][y] == 1 and game[x][y-1] == 1:
                game[x][y] = 0
                white_captured += 1
                return game[x][y]
        elif on_corner(x, y) == 'sw' and game[x][y] == 1:
            if game[x+1][y] == 2 and game[x][y-1] == 2:
                game[x][y] = 0
                black_captured += 1
                return game[x][y]
        elif on_corner(x, y) == 'sw' and game[x][y] == 2:
            if game[x+1][y] == 1 and game[x][y-1] == 1:
                game[x][y] = 0
                white_captured += 1
                return game[x][y]
        elif on_corner(x, y) == 'ne' and game[x][y] == 1:
            if game[x-1][y] == 2 and game[x][y+1] == 2:
                game[x][y] = 0
                black_captured += 1
                return game[x][y]
        elif on_corner(x, y) == 'ne' and game[x][y] == 2:
            if game[x-1][y] == 1 and game[x][y+1] == 1:
                game[x][y] == 0
                white_captured += 1
                return game[x][y]
        elif on_corner(x, y) == False and game[x][y] == 1:
            if game[x+1][y] == 2 and game[x][y+1] and game[x][y-1] == 2 and game[x-1][y] == 2:
                game[x][y] = 0
                black_captured += 1
                return game[x][y]
        elif on_corner(x, y) == False and game[x][y] == 2:
            if game[x+1][y] == 1 and game[x][y+1] and game[x][y-1] == 1 and game[x-1][y] == 1:
                game[x][y] = 0
                white_captured += 1 
                return game[x][y]
    except Exception as e: print(e)

def occupied_space(x, y):
    if game[y][x] == 0:
        return False 
    return True

def current_player_mark():
    return {'player1': '1', 'player2': '2'}.get(current_player())

def current_player_color():
    if current_player() == 2:
        return 'white'
    return 'black'

def current_player():
    global current_turn 
    current_turn = (current_turn + 1 ) % 2
    return players[current_turn]

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
def update_board(board_map = board_map, player = 0, col = -1, row = -1):
    try: 
        header_cols = []
        if board_map is not None:
            print(chr(27) + "[2J")
            for x in range(board_size):
                header_cols.append(x)
            #     print(" " + str(x) + " ", end = "")
            # print('\n')
            prGreen(header_cols)
            if row != -1 and col != -1:
                board_map[row][col] = player
            for count, row in enumerate(board_map):
                for count2, stone in enumerate(row): 
                    # pdb.set_trace()
                    # print(count2, count)
                    check_liberties(count2, count)

                    # check_adjacency(count2, count)
                if count > 0:
                    prGreen(count)
                prPurple(row)
                # print(board_map)
                # pdb.set_trace()
            return board_map
    except IndexError as e: print(e)
    except: print('sorry, something went awry')

def get_random_move():
    got_move = False
    while got_move == False:
        move_x = random.randint(1, last_index - 1)
        move_y = random.randint(1, last_index - 1)
        if occupied_space(move_x, move_y) == False and on_board(move_x, move_y):
            got_move = True
            return (move_x, move_y)
    
def get_move():
    try:
        move = input("move: ")
        if move == "p":
            return move
        if move == "r":
            return get_random_move()
        move_x = (int(move[0]))
        move_y = (int(move[1]))
        if occupied_space(move_x, move_y) == True:
            raise Exception
        if on_board(move_x, move_y) == False:
            raise Exception
        # pdb.set_trace()
        return [move_x, move_y]
    except Exception as e: print("invalid move", e)
    # get_move()


def game_loop(board_map):
    try:
        update_board()
        
        if board_map is not None:
            game_over = False
            while (game_over != True):
                if current_turn == 1:
                    new_move = get_random_move()
                    game = update_board(
                        board_map, current_player_mark(), new_move[0], new_move[1])
                    print(current_turn)

                print('your turn')
                prRed(black_captured)
                prCyan(white_captured)
                new_move = get_move()
                if new_move == 'p':
                    game = update_board()
                    current_player()
                    game_loop(game)
                if new_move is not None:
                    game = update_board(board_map, current_player_mark(), new_move[0], new_move[1])
            return game
    except TypeError as e: print(e)
    game = update_board(board_map, current_player_mark(),new_move[0], new_move[1])
game_loop(game)
