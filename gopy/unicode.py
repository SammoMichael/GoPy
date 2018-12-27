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

newline = ""
for count, x in enumerate(midline):
    if x != '┼':
        newline += (x)
    if x == '┼':
        print(count)
        newline += (black_stone)


# print(newline)


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

coordinates = [0, 4, 8, 12, 16, 20, 24, 28]
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
        yield newline
        yield inter(*row)
    yield botline


def game(squares): return "\n".join(_game(squares))


game.__doc__ = """Return the chessboard as a string for a given position.
    position is a list of 8 lists or tuples of length 8 containing integers
"""
if __name__ == "__main__":
    print(game(start_position))

# newline = ""
# for count, x in enumerate(midline):
#     if x != '┼':
#         newline += (x)
#     if x == '┼':
#         newline += ('0')
#         print(count)
        
# print(newline)

# print(newline[0: 5])
# print(tpl)
