"""
Working on a rudimentary implementation of a Chess Board Game
"""

from icecream import ic
import random
import string

error_messages = {
    'init_pos_first': 'Position must be initialized first.',
    'direction_invalid': 'Direction is invalid',
}

"""Home squares are hard coded. Neccessary to check if piece like pawn is in home square."""
home_squares = {
    'K': {'w': [(1, 5),], 'b': [(8, 5),] },
    'P': {
        'w': [(2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (2,7), (2,8)],
        'b': [(7,1), (7,2), (7,3), (7,4), (7,5), (7,6), (7,7), (7,8)]
    },
    'Q': {'w': ((1, 4),), 'b': ((8, 4),)},
    'B': {'w': ((1, 3), (1, 6)), 'b': ((8, 3), (8, 6))},
    'N': {'w': ((1, 2), (1, 7)), 'b': ((8, 2), (8, 7))},
    'R': {'w': ((1, 1), (1, 8)), 'b': ((8, 1), (8, 8))}
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
        self.active_pieces = {}
        self.full_set = [
            ['K', 1, 'w'],
            ['K', 1, 'b'],
            ['P', 8, 'w'],
            ['P', 8, 'b'],
            ['Q', 1, 'w'],
            ['Q', 1, 'b'],
            ['B', 2, 'w'],
            ['B', 2, 'b'],
            ['N', 2, 'w'],
            ['N', 2, 'b'],
            ['R', 2, 'w'],
            ['R', 2, 'b']
        ]
        self.occupied_squares = set()

    def __repr__(self):
        return f'{self.active_pieces}'


    def init_piece(self, piece_t: str, color: str, id: str | None = None):
        if id is None:
            id = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
        match piece_t:
            case 'K':
                self.active_pieces[id] = King(id)
            case 'P':
                self.active_pieces[id] = Pawn(id)
            case 'Q':
                self.active_pieces[id] = Queen(id)
            case 'B':
                self.active_pieces[id] = Bishop(id)
            case 'N':
                self.active_pieces[id] = Knight(id)
            case 'R':
                self.active_pieces[id] = Rook(id)

        self.active_pieces[id].init_color(color)
        return id


    def valid_move(self, move: list[int]) -> bool:
        """Takes move from piece and checks if the move is valid in this position"""
        return False

    def init_board(self):
        """Initializes all pieces to their home square."""
        self.active_pieces = {}

        for element in self.full_set:
            piece_t, n, color = element
            for i in range(n):
                id = self.init_piece(piece_t, color)
                last_init_piece = self.active_pieces[id]
                hs = home_squares[piece_t][color][i]
                last_init_piece.goto_square(hs)


class Piece:
    home_square = []

    def __init__(self, id):
        self.id = id
        self.color = None
        self.current_square = () # Square is a coordinate [i,j] e.g. [1,5]
        self.available_moves = []
        # If True castling is not allowed
        self.moved_yet = False


    def init_color(self, color):
        if color in ('w', 'b'):
            self.color = color
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

    def __repr__(self):
        return f'Pawn {self.id}'

    def __str__(self):
        return(f'square: {self.current_square}')

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
    def __repr__(self):
        return(f'King {self.id}')

    def get_moves(self):
        if self.current_square is not None:
            self.available_moves = []
            tmp_moves = []

        else:
            raise ValueError('%s' % error_messages['init_pos_first'])


class Queen(Piece):
    def __repr__(self):
        return(f'Queen {self.id}')

    def get_moves(self):
        return

class Bishop(Piece):
    def __repr__(self):
        return(f'Bishop {self.id}')

    def get_moves(self):
        return


class Knight(Piece):
    def __repr__(self):
        return(f'Knight {self.id}')

    def get_moves(self):
        return


class Rook(Piece):
    def __repr__(self):
        return(f'Rook {self.id}')

    def get_moves(self):
        return
