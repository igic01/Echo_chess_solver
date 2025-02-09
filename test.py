from board import board
from moves import move_sets 

# starting position
# type
# move_sets
position = (0,0)
moves = move_sets.get('K')
n_min = 0 

def get_queen_moves(board):
    """
    Generate all possible horizontal, vertical, and diagonal moves for a queen from (0, 0).

    :param board: board
    :return: List of possible moves as (row_offset, col_offset).
    """
    num_rows = len(board)
    num_cols = len(board[0])
    num_max = max(num_rows, num_cols)  # The furthest a queen can move in any direction

    moves = []
    for n in range(1, num_max):
        # Horizontal and Vertical Moves
        if n < num_cols:
            moves.append((0, n))   # Right
            moves.append((0, -n))  # Left
        if n < num_rows:
            moves.append((n, 0))   # Down
            moves.append((-n, 0))  # Up

        # Diagonal Moves
        if n < num_rows and n < num_cols:
            moves.append((n, n))   # Down-Right
            moves.append((n, -n))  # Down-Left
            moves.append((-n, n))  # Up-Right
            moves.append((-n, -n)) # Up-Left

    return moves


print(get_queen_moves(board))    
        