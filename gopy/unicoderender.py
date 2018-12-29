import sys
allbox = ''.join(chr(9472 + x) for x in range(200))
box = [allbox[i] for i in (2, 0, 12, 16, 20, 24, 44, 52, 28, 36, 60)]
(vbar, hbar, ul, ur, ll, lr, nt, st, wt, et, plus) = box
h3 = hbar * 3
topline = ul + (h3 + nt) * 7 + h3 + ur
midline = wt + (h3 + plus) * 7 + h3 + et
botline = ll + (h3 + st) * 7 + h3 + lr
pieces = '        '  # + pieces[:6][::-1] + pieces[6:]
white_stone = '○'
allbox = ''.join(chr(9472 + x) for x in range(200))
box = [allbox[i] for i in (2, 0, 12, 16, 20, 24, 44, 52, 28, 36, 60)]
black_stone =  '●'
(vbar, hbar, ul, ur, ll, lr, nt, st, wt, et, plus) = box
h3 = hbar * 3
# useful constant unicode strings to draw the square borders
topline = ul + (h3 + nt) * 7 + h3 + ur
midline = wt + (h3 + plus) * 7 + h3 + et
botline = ll + (h3 + st) * 7 + h3 + lr
tpl = u' %s ' + vbar
# coordinates = [-1]

grid = [[0, 4, 8, 12, 16, 20, 24, 28, 32],
    [68, 72, 76, 80, 84, 88, 92, 96, 100],
    [136, 140, 144, 148, 152, 156, 160, 164, 168],
    [204, 208, 212, 216, 220, 224, 228, 232, 236],
    [272, 276, 280, 284, 288, 292, 296, 300, 304],
    [340, 344, 348, 352, 356, 360, 364, 368, 372],
    [408, 412, 416, 420, 424, 428, 432, 436, 440],
    [476, 480, 484, 488, 492, 496, 500, 504, 508],
    [544, 548, 552, 556, 560, 564, 568, 572, 576],
]


#coordinates1 = [0, 4, 8, 12, 16, 20, 24, 28, 32]
#coordinates2 = [68, 72, 76, 80, 84, 88, 92, 96, 100]
#coordinates3 = [136, 140, 144, 148, 152, 156, 160, 164, 168]
#coordinates4 = [204, 208, 212, 216, 220, 224, 228, 232, 236]
#coordinates5 = [272, 276, 280, 284, 288, 292, 296, 300, 304]
#coordinates6 = [340, 344, 348, 352, 356, 360, 364, 368, 372]
#coordinates7 = [408, 412, 416, 420, 424, 428, 432, 436, 440]
#coordinates8 = [476, 480, 484, 488, 492, 496, 500, 504, 508]
#coordinates9 = [544, 548, 552, 556, 560, 564, 568, 572, 576]

# ○───○───○───○───○───○───○───○───○
# │   │   │   │   │   │   │   │   │
# ○───○───○───○───○───○───○───○───○
# │   │   │   │   │   │   │   │   │
# ○───○───○───○───○───○───○───○───○
# │   │   │   │   │   │   │   │   │
# ○───○───○───○───○───○───○───○───○
# │   │   │   │   │   │   │   │   │
# ○───○───○───○───○───○───○───○───○
# │   │   │   │   │   │   │   │   │
# ○───○───○───○───○───○───○───○───○
# │   │   │   │   │   │   │   │   │
# ○───○───○───○───○───○───○───○───○
# │   │   │   │   │   │   │   │   │
# ○───○───○───○───○───○───○───○───○
# │   │   │   │   │   │   │   │   │
# ○───○───○───○───○───○───○───○───○
# newbotline = ''
# for count, x in enumerate(botline):
#     if x == '┴' and count not in coordinates:
#         print(count)
#         newbotline += ('┴')
#     if x == '┴' or x == "┘" or x == "└" and count in coordinates:
#         print(count)
#         newbotline += (white_stone)
#     if x != '┴' and x != "┘" and x != "└":
#         newbotline += ('─')
#   
# newtopline = ''
# for count, x in enumerate(topline):
#     if x == '┬' and count not in coordinates:
#         print(count)
#         newtopline += ('┬')
#     if x == '┬'or x == "┐" or x == "┌" and count in coordinates:
#         print(count)
#         newtopline += (white_stone)
#     if x != '┬' and x != "┐" and x != "┌":
#         newtopline += (x)


# newmidline = ""
# for count, x in enumerate(midline):
#     if x == '┼' and count not in coordinates:
#         print(count)
#         newmidline += ('┼')
#     if x == '┼' or x == "├" or x == "┤" and count in coordinates:
#         print(count)
#         newmidline += (white_stone)
#     if x != '┼' and x != "├" and x != "┤":
#         newmidline += (x)

# newmidline2 = midline[0:].replace('┼', white_stone)
# print(newmidline2)
# # print(newline)

def inter(*args):
    """Return a unicode string with a line of the chessboard.
    
    args are 8 integers with the values
        0 : empty square
        1, 2, 3, 4, 5, 6: white pawn, knight, bishop, rook, queen, king
        -1, -2, -3, -4, -5, -6: same black pieces
    """
    assert len(args) == 8
    return vbar + u''.join((tpl % pieces[a] for a in args))


# print(pieces)
# print(' '.join(box))
# print
start_position = (
    [
        (-4, -2, -3, -5, -6, -3, -2, -4),
        (-1,) * 8,
    ] +
    [(0,) * 8] * 4 +
    [
        (1,) * 8,
        (4, 2, 3, 5, 6, 3, 2, 4),
    ]
)

# newnewline = list(newline)
# newnewline[5] = 'X'
# print(newnewline[4])
# for x in coordinates:
    # newnewline[x] = black_stone
    # print(newnewline[x])
# sys.stdout.write(str(newnewline))

def _game(position):
    yield topline
    yield inter(*position[0])
    for row in position[1:]:
        # yield str(newnewline)
        yield midline
        yield inter(*row)
    yield botline


def game(squares): return "\n".join(_game(squares))


game.__doc__ = """Return the chessboard as a string for a given position.
    position is a list of 8 lists or tuples of length 8 containing integers
"""
if __name__ == "__main__":
    print(game(start_position))

