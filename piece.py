import copy
from board import board

class Piece:
    def __init__(self, name, moves, position):
        self.name = name
        self.color = name[0]
        self.moves = moves
        self.position = position
        self.capture_positions = set()
        self.num_of_capturable_pieces = 0

        # Process movement and capturing
        self.analyze_captures(position, copy.deepcopy(board))

    def analyze_captures(self, position, board):
        """ Determines the possible captures for a piece. """
        row, col = position
        board[row][col] = '_'  # Remove the piece from the board to analyze moves
        
        # Count capturable pieces once
        self.num_of_capturable_pieces = self.count_capturable_pieces(board)
        
        if self.name[1] == 'P':  # Pawn has different capture logic
            self.pawn_captures(position, board)
        else:
            self.standard_captures(position, board)

    def standard_captures(self, position, board):
        """ Generic capture logic for all non-pawn pieces. """
        row, col = position
        if len(self.capture_positions) >= self.num_of_capturable_pieces:
            return

        if not (0 <= row < len(board) and 0 <= col < len(board[0])):
            return  # Out of bounds

        cell = board[row][col]
        if cell == 'X':
            return  # Already visited

        if cell != '_':  # Enemy piece found
            board[row][col] = 'X' # Mark visited
            if cell[0] == 'b': # Check if enemy piece
                self.capture_positions.add((row, col))
            return

        board[row][col] = 'X'  # Mark visited

        # Recursively explore further moves
        for d_row, d_col in self.moves:
            self.standard_captures((row + d_row, col + d_col), copy.deepcopy(board))

    def pawn_captures(self, position, board):
        """ Special case: Pawn captures diagonally, moves forward. """
        row, col = position
        for i in range(row, 0, -1):
            len_col = len(board[i])
            if 0 <= col - 1 < len_col and board[i - 1][col - 1][0] == 'b':
                self.capture_positions.add((i - 1, col - 1))
            if 0 <= col + 1 < len_col and board[i - 1][col + 1][0] == 'b':
                self.capture_positions.add((i - 1, col + 1))
            if board[i - 1][col]!= '_':
                break  # No more possible captures

    @staticmethod
    def count_capturable_pieces(board):
        """ Counts capturable black pieces on the board. """
        return sum(1 for row in board for cell in row if cell[0] in {'w', 'b'})

    def __str__(self):
        return f"{self.name} at {self.position}, Captures: {self.capture_positions}"
