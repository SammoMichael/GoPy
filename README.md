GoPy is the game of go in Python

In order to provide more options I am working on 3 versions of Go:
* Without Unicode characters, the most basic but most versatile, you can choose a board almost any size
* A simple board display in Unicode, will be available in standard 9x9, 13x13, or 19x19
* Finally, a GUI using Pygame

![Screenshot](https://github.com/SammoMichael/GoPy/blob/master/unicode2.png)

## Technologies
Python

```python
def game_loop(board_map):
    try:
        update_board()
        if board_map is not None:
            game_over = False
            while (game_over != True):
                if current_turn == 2:
                    print("2")
                    new_move = get_random_move()
                    game = update_board(
                        board_map, current_player_mark(), new_move[0], new_move[1])

                new_move = get_move()
                if new_move is not None:
                    game = update_board(board_map, current_player_mark(), new_move[0], new_move[1])
            return game
    except TypeError as e: print(e)
    game = update_board(board_map, current_player_mark(),new_move[0], new_move[1])
game_loop(game)
```

### Instructions
clone and run in terminal
