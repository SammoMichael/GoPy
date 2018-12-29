import time 
import sys
import pdb 
import numpy as np
import random
import unicoderender as uc
import datetime
import threading
# import cursor

def prRed(prt): print("\033[91m {}\033[00m" .format(prt))
def prGreen(prt): print("\033[92m {}\033[00m" .format(prt))
def prYellow(prt): print("\033[93m {}\033[00m" .format(prt))
def prLightPurple(prt): print("\033[94m {}\033[00m" .format(prt))
def prPurple(prt): print("\033[95m {}\033[00m" .format(prt))
def prCyan(prt): print("\033[96m {}\033[00m" .format(prt))
def prLightGray(prt): print("\033[97m {}\033[00m" .format(prt))
def prBlack(prt): print("\033[98m {}\033[00m" .format(prt))
# board_size = int(input("board size?")
game_start_time = datetime.datetime.now()
game_time = datetime.datetime.now() - game_start_time
white_played_stones = []
black_played_stones = []
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
white_real_groups = []
grouped_groups = []

def check_adjacency(pos, pos2):
    # pdb.set_trace()
    if abs(pos[0] - pos2[0]) <= 1 ^ abs(pos[1] - pos2[1]) <= 1 and pos2[0] != pos2[1]:
        
        return True 
    return False

def check_groups():
    # pdb.set_trace()
    for count, pos in enumerate(white_played_stones):
        for count2, pos2 in enumerate(white_played_stones):
            if check_adjacency(pos, pos2) == True and pos not in white_groups and pos != pos2:
                white_groups.append(pos)
            elif check_adjacency(pos, pos2) == True and pos2 not in white_groups and pos != pos2:
                white_groups.append(pos2)     
    for count, pos in enumerate(black_played_stones):
        for count2, pos2 in enumerate(black_played_stones):
            if check_adjacency(pos, pos2) == True and pos not in black_groups and pos != pos2:
                black_groups.append(pos)     
            elif check_adjacency(pos, pos2) == True and pos2 not in black_groups and pos != pos2:
                black_groups.append(pos2)   
    group_groups()
    add_to_groups()
    combine_groups()

def add_to_groups():
    # pdb.set_trace()
    for count, pos in enumerate(white_groups):
        for count2, groups in enumerate(white_real_groups):
            # print(groups)
            if pos not in groups:
                for pos2 in groups:
                    print(pos)
                    if check_adjacency(pos, pos2) == True:

                      print(True)
                      # print(pos)
                      # print(pos2)
                      print(white_real_groups[count2].append(pos))
                      break
                      # white_real_groups[count2].append(pos2)
                    #     continue
    print(white_real_groups)


def combine_groups():

    for count, pos in enumerate(white_groups):
      trues = 0
      for count2, groups in enumerate(white_real_groups):
        if (pos in groups):
          trues += 1
          print(trues)
        if trues == len(white_real_groups):
          print('yaay' + str(pos))
          print(trues)

    print(white_real_groups)
    print(len(white_real_groups))


def count_liberty():
    pass



# def group_liberties():
#     for count, pos in enumerate(white_groups):
#             for count2, pos2 in enumerate(white_groups):
#                 if pos != pos2 and check_adjacency(pos, pos2) == True:
#                     white_real_groups.concat([pos, pos2])


def group_groups():
    global grouped_groups
    global white_real_groups
    # pdb.set_trace()
    global white_real_groups
    white_real_groups.clear()
    for count, pos in enumerate(white_groups[:-1]):
        if pos not in grouped_groups:
            if check_adjacency(white_groups[count], white_groups[count + 1] ) == True and [white_groups[count]] not in white_real_groups:
                if len(grouped_groups) == 0:
                    white_real_groups = [white_groups[count], white_groups[count+1]]
                    continue
                elif len(grouped_groups) > 0:
                    white_real_groups += [[white_groups[count], white_groups[count+1]]]
                    continue
            # white_real_groups += white_groups[count]
    if white_real_groups not in grouped_groups and white_real_groups != []: 
        if len(white_real_groups) != 0:
            # grouped_groups += [white_real_groups]
            grouped_groups.append(white_real_groups)


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
        global game_time
        print("\u001b[96mHelloWorld")
        print("\u001b[40m {% game %}")
        # print(chr(27) + "[2J")

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
                print(chr(27) + "[2J")

                if current_turn % 2 == 1:
                    newmap = game[:(idx)] + game[idx].replace(game[idx], uc.black_stone, 1) + game[(idx + 1):]
                    game = newmap
                elif current_turn % 2 == 0:
                    newmap = game[:(idx)] + game[idx].replace(game[idx], uc.white_stone, 1) + game[(idx + 1):]
                    game = newmap
                print(newmap)
                print(white_captured)
                print(black_captured)
                now = datetime.datetime.now()
                print(now.second - game_start_time.second)
         
                # pdb.set_trace()
                # for count2, stone in enumerate(row): 
                    # print(count2, count)
                check_groups()
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
                # print(chr(27) + "[2J")

                print(game)
                # print(white_captured)
                # print(black_captured)
                # print(black_played_stones)
                # print("black groups:" + str(black_groups))
                print("white groups:" + str(white_groups))
                print("white real groups:" + str(white_real_groups))
                # print("grouped_groups:" + str(grouped_groups))
                # print(white_played_stones)

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
    time.sleep(3)
    got_move = False
    while got_move == False:
        move_x = random.randint(1, last_index - 1)
        move_y = random.randint(1, last_index - 1)
        if occupied_space(move_x, move_y) == False and on_board(move_x, move_y):
            got_move = True
            return (move_x, move_y)
    
def get_move():
    try:
        # move = ""
        # while move == "":
            
        # change = datetime.datetime.now() - game_start_time
        # print('\033[1;1H' + time.asctime(time.localtime())
                # )
            #   (str(change)[5:7])
        # print(now.strftime("%H:%M:%S"), end="\r")
        # sys.stdout.flush()
        # time.sleep(.4)
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
        print('\033[1;1H' + time.asctime(time.localtime())
                )
        return (move_x, move_y)
    except Exception as e: print("invalid move", e)
    get_move()


def game_loop(board_map):
    try:
        global played_stones
        global game_over
        if board_map is not None:
            update_board()
            game_over = False
            while (game_over != True):
                if current_turn % 2 == 0:
                    new_move = get_random_move()
                    # new_move = get_move()
                    white_played_stones.append(new_move)

                    game = update_board(
                        board_map, current_player_mark(), new_move[0], new_move[1])
                    # print(current_turn)

                # print('your turn')
                # prRed(black_captured)
                # prCyan(white_captured)
                new_move = get_move()
                if new_move == 'r':
                    new_move = get_random_move()
                    # new_move = get_move()
                    black_played_stones.append(new_move)
                    game = update_board(
                    board_map, current_player_mark(), new_move[0], new_move[1])
                if new_move == 'p':
                    game = update_board()
                    current_player()
                    # game_loop(game)
                if new_move is not None and new_move != 'p': 
                    black_played_stones.append(new_move)
                    game = update_board(board_map, current_player_mark(), new_move[0], new_move[1])
            return game
    except TypeError as e: print(e)
    if game != None and new_move != None:    
        game = update_board(game, current_player_mark(),new_move[0], new_move[1])
while game != None:
    game_loop(game)
