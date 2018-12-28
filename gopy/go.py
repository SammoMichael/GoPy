
import sys
import pdb 
import numpy as np
import random
import unicoderender as uc

def prRed(prt): print("\033[91m {}\033[00m" .format(prt))
def prGreen(prt): print("\033[92m {}\033[00m" .format(prt))
def prYellow(prt): print("\033[93m {}\033[00m" .format(prt))
def prLightPurple(prt): print("\033[94m {}\033[00m" .format(prt))
def prPurple(prt): print("\033[95m {}\033[00m" .format(prt))
def prCyan(prt): print("\033[96m {}\033[00m" .format(prt))
def prLightGray(prt): print("\033[97m {}\033[00m" .format(prt))
def prBlack(prt): print("\033[98m {}\033[00m" .format(prt))
# board_size = int(input("board size?"))
game_over = False
board_size = 9
board_map = np.zeros( (board_size, board_size) )
last_index = board_size - 1
game = (uc.game(uc.start_position))
board_map = (uc.game(uc.start_position))
players = ['player1', 'player2']
turns = [0, 1]
current_turn = 1
white_captured = 0
black_captured = 0
turn_count = 0
map = (uc.game(uc.start_position))

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

def check_liberties(pos):
    # pdb.set_trace()
    x, y = unflatten(pos)
    # pdb.set_trace()
    try: 
        idx = flatten(x, y)
        # top = flatten(x, y-1)
        # bot = flatten(x, y+1)
        # left = flatten(x-1, y)
        # right = flatten(x+1, y)
        global white_captured
        global black_captured
        global game
        # pdb.set_trace()

        if on_corner(x, y) == 's' and game[idx] == uc.white_stone:

            top = flatten(x, y-1)
            left = flatten(x-1, y)
            right = flatten(x+1, y)
            if game[top] == uc.black_stone and game[right] == uc.black_stone and game[left] == uc.black_stone:
                # pdb.set_trace()

                game = game[:(idx)] + game[idx].replace(game[idx], '┴', 1) + game[(idx + 1):]
                white_captured += 1
                return game
        elif on_corner(x, y) == 's' and game[idx] == uc.black_stone:
            top = flatten(x, y-1)
            left = flatten(x-1, y)
            right = flatten(x+1, y)
            if game[top] == uc.white_stone and game[right] == uc.white_stone and game[left] == uc.white_stone:
                game = game[:(idx)] + game[idx].replace(game[idx], '┴', 1) + game[(idx + 1):]
                black_captured += 1
                return game
        elif on_corner(x, y) == 'n' and game[idx] == uc.white_stone:
            bot = flatten(x, y+1)
            left = flatten(x-1, y)
            right = flatten(x+1, y)
            if game[bot] == uc.black_stone and game[right] == uc.black_stone and game[left] == uc.black_stone:
                game = game[:(idx)] + game[idx].replace(game[idx], '┬', 1) + game[(idx + 1):]
                white_captured += 1
                return game
        elif on_corner(x, y) == 'n' and game[idx] == uc.black_stone:
            bot = flatten(x, y+1)
            left = flatten(x-1, y)
            right = flatten(x+1, y)
            if game[bot] == uc.white_stone and game[right] == uc.white_stone and game[left] == uc.white_stone:
                game = game[:(idx)] + game[idx].replace(game[idx], '┬', 1) + game[(idx + 1):]
                black_captured += 1
                return game
        elif on_corner(x, y) == 'e' and game[idx] == uc.white_stone:
            top = flatten(x, y-1)
            bot = flatten(x, y+1)
            left = flatten(x-1, y)
            if game[left] == uc.black_stone and game[bot] == uc.black_stone and game[top] == uc.black_stone:
                game = game[:(idx)] + game[idx].replace(game[idx], "├", 1) + game[(idx + 1):]
                white_captured += 1
                return game
        elif on_corner(x, y) == 'e' and game[idx] == uc.black_stone:
            top = flatten(x, y-1)
            bot = flatten(x, y+1)
            left = flatten(x-1, y)
            if game[left] == uc.white_stone and game[top] == uc.white_stone and game[bot] == uc.white_stone:
                game = game[:(idx)] + game[idx].replace(game[idx], "├", 1) + game[(idx + 1):]
                black_captured += 1
                return game
        elif on_corner(x, y) == 'w' and game[idx] == uc.white_stone:
            right = flatten(x+1, y)
            top = flatten(x, y-1)
            bot = flatten(x, y+1)
            if game[right] == uc.black_stone and game[top] == uc.black_stone and game[bot] == uc.black_stone:
                game = game[:(idx)] + game[idx].replace(game[idx], "┤", 1) + game[(idx + 1):]
                white_captured += 1
                return game
        elif on_corner(x, y) == 'w' and game[idx] == uc.black_stone:
            right = flatten(x+1, y)
            top = flatten(x, y-1)
            bot = flatten(x, y+1)
            if game[right] == uc.white_stone and game[top] == uc.white_stone and game[bot] == uc.white_stone:
                game = game[:(idx)] + game[idx].replace(game[idx], "┤", 1) + game[(idx + 1):]
                black_captured += 1
                return game
        elif on_corner(x, y) == 'nw' and game[idx] == uc.white_stone:
            bot = flatten(x, y+1)
            right = flatten(x+1, y)
            if game[right] == uc.black_stone and game[bot] == uc.black_stone:
                game = game[:(idx)] + game[idx].replace(game[idx], "┌", 1) + game[(idx + 1):]
                white_captured += 1
                return game
        elif on_corner(x, y) == 'nw' and game[idx] == uc.black_stone:
            bot = flatten(x, y+1)
            right = flatten(x+1, y)
            if game[right] == uc.white_stone and game[bot] == uc.white_stone:
                game = game[:(idx)] + game[idx].replace(game[idx], "┌", 1) + game[(idx + 1):]
                black_captured += 1
                return game
        elif on_corner(x, y) == 'se' and game[idx] == uc.black_stone:
            top = flatten(x, y-1)
            left = flatten(x-1, y)
            if game[left] == uc.white_stone and game[top] == uc.white_stone:
                game = game[:(idx)] + game[idx].replace(game[idx], "┘", 1) + game[(idx + 1):]
                black_captured += 1
                return game
        elif on_corner(x, y) == 'se' and game[idx] == uc.white_stone:
            top = flatten(x, y-1)
            left = flatten(x-1, y)
            if game[left] == uc.black_stone and game[top] == uc.black_stone:
                game = game[:(idx)] + game[idx].replace(game[idx], "┘", 1) + game[(idx + 1):]
                white_captured += 1
                return game
        elif on_corner(x, y) == 'sw' and game[idx] == uc.black_stone:
            top = flatten(x, y-1)
            right = flatten(x+1, y)
            if game[right] == uc.white_stone and game[top] == uc.white_stone:
                game = game[:(idx)] + game[idx].replace(game[idx], "└", 1) + game[(idx + 1):]
                black_captured += 1
                return game
        elif on_corner(x, y) == 'sw' and game[idx] == uc.white_stone:
            top = flatten(x, y-1)
            right = flatten(x+1, y)
            if game[right] == uc.black_stone and game[top] == uc.black_stone:
                game = game[:(idx)] + game[idx].replace(game[idx], "└", 1) + game[(idx + 1):]
                white_captured += 1
                return game
        elif on_corner(x, y) == 'ne' and game[idx] == uc.black_stone:
            bot = flatten(x, y+1)
            left = flatten(x-1, y)
            if game[left] == uc.white_stone and game[bot] == uc.white_stone:
                game = game[:(idx)] + game[idx].replace(game[idx], "┐", 1) + game[(idx + 1):]
                black_captured += 1
                return game
        elif on_corner(x, y) == 'ne' and game[idx] == uc.white_stone:
            bot = flatten(x, y+1)
            left = flatten(x-1, y)
            if game[left] == uc.black_stone and game[bot] == uc.black_stone:
                game = game[:(idx)] + game[idx].replace(game[idx], "┐", 1) + game[(idx + 1):]
                white_captured += 1
                return game
        elif on_corner(x, y) == False and game[idx] == uc.black_stone:
            top = flatten(x, y-1)
            bot = flatten(x, y+1)
            left = flatten(x-1, y)
            right = flatten(x+1, y)
            if game[right] == uc.white_stone and game[bot] == uc.white_stone and game[top] == uc.white_stone and game[right] == uc.white_stone:
                game = game[:(idx)] + game[idx].replace(game[idx], '┼', 1) + game[(idx + 1):]
                black_captured += 1
                return game
        elif on_corner(x, y) == False and game[idx] == uc.white_stone:
            top = flatten(x, y-1)
            bot = flatten(x, y+1)
            left = flatten(x-1, y)
            right = flatten(x+1, y)
            if game[right] == uc.black_stone and game[bot] == uc.black_stone and game[top] == uc.black_stone and game[left] == uc.black_stone:
                game = game[:(idx)] + game[idx].replace(game[idx], '┼', 1) + game[(idx + 1):]
                white_captured += 1 
                return game
        return game
    except Exception as e: print(e)

def occupied_space(x, y):
    idx = flatten(x, y)
    # pdb.set_trace()
    if game[idx] == uc.black_stone or game[idx] == uc.white_stone:
        return True 
    return False

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

def unflatten(pos):
    y = int(pos / 68)
    x = int(pos % 68 / 4)
    if x <= board_size and y <= board_size:
        return [x, y]

def flatten(x, y):
    idx = uc.grid[y][x]
    return idx
# def unflatten(idx)

def update_board(board_map = board_map, player = 0, col = -1, row = -1):
    try: 
        if board_map is not None:
            global turn_count
            global game
            header_cols = []
            print(chr(27) + "[2J")
            for x in range(board_size):
                header_cols.append(x)
                print("" + str(x) + "   ", end = "")
            print('')
            # prGreen(header_cols)
            if row == -1:
                print(game)
                print(white_captured)
                print(black_captured)
                return game
            if row != -1 and col != -1:
                # pdb.set_trace()

                idx = uc.grid[row][col] 
                # uc.start_position = player
            # for count, row in enumerate(uc.game(uc.start_position)):
                # map = (uc.game(uc.start_position))
                if current_turn % 2 == 1:
                    newmap = game[:(idx)] + game[idx].replace(game[idx], uc.black_stone, 1) + game[(idx + 1):]
                    game = newmap
                elif current_turn % 2 == 0:
                    newmap = game[:(idx)] + game[idx].replace(game[idx], uc.white_stone, 1) + game[(idx + 1):]
                    game = newmap
                print(newmap)
                print(white_captured)
                print(black_captured)
                # pdb.set_trace()
                # for count2, stone in enumerate(row): 
                    # print(count2, count)
                for row in uc.grid: 
                    # print(count)
                    for count in row:
                        mappedCount = count % 68
                        if mappedCount <= 32 and mappedCount % 4 == 0 and count <= 576:
                            # pdb.set_trace()

                            # print(count)
                            # posx, posy = unflatten(count) 
                            # print(x, y)
                            if game[count] == uc.black_stone or game[count] == uc.white_stone:    
                                check_liberties(count)
                for x in range(board_size):
                    header_cols.append(x)
                    print("" + str(x) + "   ", end="")
                print('')
                    # prGreen(header_cols)
                print(game)
                print(white_captured)
                print(black_captured)
                    # check_adjacency(count2, count)
                # if count > 0:
                #     prGreen(count)
                    # print(uc.game(uc.start_position))
                # prPurple(row)
                # print(board_map)
                # pdb.set_trace()
            game = newmap
            board_map = newmap
            turn_count += 1
            return newmap
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
        # update_board()
        # prRed(black_captured)
        # prCyan(white_captured)
        print(int(turn_count))
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
    get_move()


def game_loop(board_map):
    try:
        global game_over
        if board_map is not None:
            update_board()
            game_over = False
            while (game_over != True):
                if current_turn == 1:
                    # new_move = get_random_move()
                    new_move = get_move()
                    game = update_board(
                        board_map, current_player_mark(), new_move[0], new_move[1])
                    # print(current_turn)

                # print('your turn')
                # prRed(black_captured)
                # prCyan(white_captured)
                new_move = get_move()
                if new_move == 'p':
                    game = update_board()
                    current_player()
                    game_loop(game)
                if new_move is not None:
                    game = update_board(board_map, current_player_mark(), new_move[0], new_move[1])
            return game
    except TypeError as e: print(e)
    if game != None and new_move != None:    
        game = update_board(game, current_player_mark(),new_move[0], new_move[1])
while game != None:
    game_loop(game)
