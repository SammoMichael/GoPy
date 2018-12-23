import sys

def prRed(prt): print("\033[91m {}\033[00m" .format(prt))
def prGreen(prt): print("\033[92m {}\033[00m" .format(prt))
def prYellow(prt): print("\033[93m {}\033[00m" .format(prt))
def prLightPurple(prt): print("\033[94m {}\033[00m" .format(prt))
def prPurple(prt): print("\033[95m {}\033[00m" .format(prt))
def prCyan(prt): print("\033[96m {}\033[00m" .format(prt))
def prLightGray(prt): print("\033[97m {}\033[00m" .format(prt))
def prBlack(prt): print("\033[98m {}\033[00m" .format(prt))

board_map = [
    ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0']
]

game = board_map
players = ['player1', 'player2']
turns = [0, 1]
current_turn = 1

def current_player_mark():
    return {'player1': '1', 'player2': '2'}.get(current_player())


def current_player():
    global current_turn 
    current_turn += 1
    print(players[(current_turn) % 2])
    return players[(current_turn) % 2]


def check_valid_move(x, y):
    return valid_move(x, y)


def valid_move(x, y):
    global board_map
    if board_map[x][y] == 1 or board_map[x][y] == 2:
        return False
    return True


def update_board(board_map, player = 0, row = 0, col = 0):
    try: 
        # print(chr(27) + "[2J")
        prGreen('   0  1  2  3  4  5  6  7  8')
        board_map[row][col] = player
        for count, row in enumerate(board_map):
            prRed(row)
            prGreen(count)
            print(board_map)
        return board_map or ''
    except IndexError as e: print(e)
    except: print('sorry, something went awry')


def get_move():
    try:
        move = input("move")
        move_x = (int(move[0]))
        move_y = (int(move[1]))
        valid = (valid_move(move_x, move_y))
        if valid == False:
            raise ValueError() 
        print([move_x, move_y])           
        return [move_x, move_y] or ''
    except Exception as e: print("invalid move", e)
    get_move()


def game_loop(board_map):
    try:
        game_over = False
        while (game_over != True):
            new_move = get_move()
            game = update_board(board_map, current_player_mark(), new_move[0], new_move[1])
        print(game)
        return game or ''
    except TypeError as e: print(e)
    raise

game_loop(game)
