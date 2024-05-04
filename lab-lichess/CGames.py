"""
Working on a rudimentary implementation of a Chess Board Game
"""

error_messages = {
    'init_pos_first': 'Position must be initialized first.',
    'direction_invalid': 'Direction is invalid',
}

class CGame:
    def __init__(self):
        self.current_board = None
        self.winner = None
        self.time_control = 'blitz'
        self.turn_count = 0
        self.board_history = []
        self.players_turn = 'w'


class Board:
    def __init__(self):
        self.players_turn = 'w'
        self.estimation = 0.0
        self.all_available_moves = []
        self.position = []


    def valid_move(self, move: list[int]) -> bool:
        """Takes move from piece and checks if the move is valid in this position"""
        return False


    def init_board(self):
        """Initializes all pieces on their home square."""
        return



class Piece:
    home_square = []

    def __init__(self):
        self.color = None
        self.current_square = [] # Square is a coordinate [i,j] e.g. [1,]
        self.available_moves = []


    def init_color(self, col):
        if col in ('w', 'b'):
            self.color = col
        else:
            raise ValueError('Color invalid')


    def goto_square(self, coord: list[int]):
        self.current_square = coord


    # [i, j] <- [ranks, files]
    def move_1_up(self, start: list[int]):
        i, j = start
        if self.color == 'w':
            return (i+1, j)
        return (i-1, j)


    def move_x_up(self, start: list[int], x: int):
        """This method is primarily for pawns. It distinguishes between piece colors and only moves forward."""
        i, j = start
        if self.color == 'w':
            return (i+x, j)
        return (i-x, j)


    def move_x_in_y(self, start: list[int], x: int, y: str):
        """
        y: str... direction like n (north), s (sourth), ne (northeast)
        Different to move_x_up this function will only consider one board direction, white pieces in south and black pieces north.
        """
        i, j = start

        if y == 'n':
            return (i + x, j)
        elif y == 's':
            return (i - x, j)
        elif y == 'e':
            return (i, j + x)
        elif y == 'w':
            return (i, j - x)
        elif y == 'ne':
            return (i + x, j + x)
        elif y == 'nw':
            return (i + x, j - x)
        elif y == 'se':
            return (i - x, j + x)
        elif y == 'sw':
            return (i - x, j - x)
        else:
            raise ValueError()



class Pawn(Piece):
    """Pawn only move straight forward by one square. Starting from the initial sqaure they have an additional opportunity to move two squares forward."""
    home_square = [
        [2,1], [2,2], [2,3], [2,4], [2,5], [2,6], [2,7], [2,8],
        [7,1], [7,2], [7,3], [7,4], [7,5], [7,6], [7,7], [7,8]
    ]

    def __str__(self):
        return("%s" % self.current_square)

    def get_moves(self):
        if self.current_square is not None:
            self.avail_moves = []
            tmp_moves = []
            tmp_moves.append(self.move_x_up(self.current_square, 1))
            tmp_moves.append(self.move_x_up(self.current_square, 2))
            self.avail_moves = tmp_moves
        else:
            raise ValueError('%s' % error_messages['init_pos_first'])
    # TODO: promotion


class King(Piece):
    """King piece has the most restrictions. It can move in all directions by one square. But it can not move on a square where it would be threatened."""

    def get_moves(self):
        if self.current_square is not None:
            self.available_moves = []
            tmp_moves = []

        else:
            raise ValueError('%s' % error_messages['init_pos_first'])
