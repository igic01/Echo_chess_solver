from board import board  # Importing the board configuration
from piece import Piece  # Importing the Piece class
from moves import move_sets  # Importing predefined move sets for pieces

# List to store all the pieces present on the board
all_pieces = []

# Loop through the board to initialize all pieces
for row in range(len(board)):
    for col in range(len(board[row])):
        if board[row][col] and board[row][col][0] in {'w', 'b'}:  # Checking if a valid piece exists
            name = board[row][col]  # Piece name (e.g., 'wP' for white pawn)
            moves = move_sets.get(name[1])  # Retrieve movement rules based on piece type
            position = (row, col)  # Store the piece's position
            piece = Piece(name, moves, position)  # Create a piece object
            all_pieces.append(piece)  # Add it to the list of all pieces

def find_eating_order(white_pieces, black_pieces, path=[]):
    """
    Recursively finds an order in which white pieces can capture all black pieces.
    
    :param white_pieces: List of white pieces.
    :param black_pieces: List of black pieces.
    :param path: List tracking the sequence of captures.
    :return: A list representing the capture sequence or None if not possible.
    """

    if not black_pieces:  # If no black pieces remain, return the path
        return path

    for w in white_pieces[:]:  # Iterate over a copy to avoid modifying during iteration
        for b in black_pieces[:]:  # Iterate over a copy to avoid modification issues
            if can_eat(w, b):  # Check if the white piece can capture the black piece
                new_white_pieces = white_pieces[:]  # Copy list to avoid modifying the original
                new_black_pieces = black_pieces[:]  # Shallow copy is allowed, because we are not editing the pieces

                new_white_pieces.remove(w)
                new_black_pieces.remove(b)
                new_white_pieces.append(b)  # The captured black piece becomes white

                new_path = path + [f"{w.name}({w.position}) -> {b.name}({b.position})"]
                result = find_eating_order(new_white_pieces, new_black_pieces, new_path)
                if result:
                    return result  # Return the first found valid sequence

    return None  # Return None if no valid capture sequence exists

def can_eat(white_piece, black_piece):
    """
    Checks if a white piece can capture a black piece.
    
    :param white_piece: The attacking white piece.
    :param black_piece: The target black piece.
    :return: True if the white piece can capture the black piece, otherwise False.
    """
    return black_piece.position in white_piece.capture_positions  # Check capture range

# Separate the pieces by color
white_pieces = [piece for piece in all_pieces if piece.color == 'w']
black_pieces = [piece for piece in all_pieces if piece.color == 'b']

# Output the solution
print(find_eating_order(white_pieces, black_pieces))
