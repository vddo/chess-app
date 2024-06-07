"""
Working on a rudimentary implementation of a Chess Board Game
"""

# from icecream import ic
import random
import string

type Square_t = tuple[int, int]

error_messages = {
    "init_pos_first": "Position must be initialized first.",
    "direction_invalid": "Direction is invalid",
}

"""
Home squares are hard coded. Neccessary to check if piece like pawn is in home
square.
"""
home_squares = {
    "K": {
        "w": [
            (1, 5),
        ],
        "b": [
            (8, 5),
        ],
    },
    "P": {
        "w": [(2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8)],
        "b": [(7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8)],
    },
    "Q": {"w": ((1, 4),), "b": ((8, 4),)},
    "B": {"w": ((1, 3), (1, 6)), "b": ((8, 3), (8, 6))},
    "N": {"w": ((1, 2), (1, 7)), "b": ((8, 2), (8, 7))},
    "R": {"w": ((1, 1), (1, 8)), "b": ((8, 1), (8, 8))},
}


class CGame:
    def __init__(self):
        self.current_board = None
        self.winner = None
        self.time_control = "blitz"
        self.turn_count = 0
        self.board_history = []
        self.players_turn = "w"


class Board:
    def __init__(self):
        self.id = None
        self.players_turn = "w"
        self.estimation = 0.0
        self.all_available_moves = []
        self.position = None
        self.active_pieces = {}
        self.full_set = [
            ["K", 1, "w"],
            ["K", 1, "b"],
            ["P", 8, "w"],
            ["P", 8, "b"],
            ["Q", 1, "w"],
            ["Q", 1, "b"],
            ["B", 2, "w"],
            ["B", 2, "b"],
            ["N", 2, "w"],
            ["N", 2, "b"],
            ["R", 2, "w"],
            ["R", 2, "b"],
        ]
        self.occupied_squares = set()

    def __repr__(self):
        return f"{self.active_pieces}"

    def init_piece(self, piece_t: str, color: str, id: str | None = None):
        if id is None:
            id = "".join(
                random.choices(
                    string.ascii_letters + string.ascii_letters + string.digits, k=4
                )
            )
        match piece_t:
            case "K":
                self.active_pieces[id] = King(id)
            case "P":
                self.active_pieces[id] = Pawn(id)
            case "Q":
                self.active_pieces[id] = Queen(id)
            case "B":
                self.active_pieces[id] = Bishop(id)
            case "N":
                self.active_pieces[id] = Knight(id)
            case "R":
                self.active_pieces[id] = Rook(id)

        self.active_pieces[id].init_color(color)
        return id

    def init_board(self):
        """
        Initializes all pieces to their home square.
        """
        self.active_pieces = {}
        self.position = Position(0)

        for element in self.full_set:
            piece_t, n, color = element
            for i in range(n):
                id = self.init_piece(piece_t, color)
                last_init_piece = self.active_pieces[id]
                hs = home_squares[piece_t][color][i]
                last_init_piece.goto_square(hs)
                # TODO: init piece id to position
                self.position.set_piece(hs, id)

    def valid_move(self, move: list[int]) -> bool:
        """
        Takes move from piece and checks if the move is valid in this position
        """
        # TODO: Need class Position
        return False


class Position:
    """
    Arguments:
    halfturn... keeps count what number of piece move was made that resulted to
    current position.
    move... the move that lead to this position.
    ancestor... position before last move was made. Only initial position
    without any move made would have no ancestor. Instance of Position inherits
    position from ancestor as a result of the last move.
    """

    def __init__(self, halfturn: int, ancestor=None):
        self.halfturn = halfturn
        self.position = dict()
        self.ancestor = ancestor
        self.init_position()

    def init_position(self):
        if self.ancestor is None:
            for i in range(1, 9):
                for j in range(1, 9):
                    self.position[(i, j)] = None
        else:
            self.position = self.ancestor.passon_position()
            # TODO: apply move

    def passon_position(self):
        return self.position

    def set_piece(self, square: Square_t, id: str):
        self.position[square] = id
        return

    def get_piece(self, square: Square_t):
        return self.position[square]


class Piece:
    def __init__(self, id):
        self.id = id
        self.color = None
        self.current_square = (0, 0)  # Square is a coordinate [i,j] e.g. [1,5]
        self.available_moves = []
        # If True castling is not allowed
        self.moved_yet = False

    def init_color(self, color):
        if color in ("w", "b"):
            self.color = color
        else:
            raise ValueError("Color invalid")

    def goto_square(self, square: Square_t):
        self.current_square = square

    # [i, j] <- [ranks, files]
    def move_1_up(self, start):
        i, j = start
        if self.color == "w":
            return (i + 1, j)
        return (i - 1, j)

    def move_x_up(self, square_origin, x: int) -> Square_t:
        """This method is primarily for pawns. It distinguishes between piece
        colors and only moves forward."""
        if self.square_is_valid(square_origin) is False:
            raise Exception("Square not valid.")

        i, j = square_origin
        if self.color == "w":
            return (i + x, j)
        return (i - x, j)

    def move_x_in_y(self, square_origin: Square_t, x: int, y: str) -> Square_t:
        """
        y: str... direction like n (north), s (sourth), ne (northeast)
        Different to move_x_up: This function will only consider one board
        direction, white pieces in south and black pieces north.
        Can move straight and diagonally.
        """
        if self.square_is_valid(square_origin) is False:
            raise Exception("Square not valid.")

        i, j = square_origin

        if y == "n":
            return (i + x, j)
        elif y == "s":
            return (i - x, j)
        elif y == "e":
            return (i, j + x)
        elif y == "w":
            return (i, j - x)
        elif y == "ne":
            return (i + x, j + x)
        elif y == "nw":
            return (i + x, j - x)
        elif y == "se":
            return (i - x, j + x)
        elif y == "sw":
            return (i - x, j - x)
        else:
            raise ValueError('Second argument must be a direction like "n", "se".')

    def square_is_valid(self, square: Square_t) -> bool:
        if len(square) != 2:
            return False

        i, j = square
        if i < 1 or j < 1 or i > 8 or j > 8:
            return False

        return True

    def to_boarder_straight(self, square: tuple) -> list[tuple[int, str]]:
        """
        Gets how many squares are to boarder in each direction n, s, w, e.
        """
        i, j = square
        to_east = 8 - j
        to_west = j - 1
        to_south = i - 1
        to_north = 8 - i
        to_boarder = [(to_east, "e"), (to_west, "w"), (to_north, "n"), (to_south, "s")]
        return to_boarder

    def get_squares_straight(self, square_original: Square_t) -> set[Square_t]:
        """
        Get all squares in same file and rank except current square.
        Return as set of tuples because elements (tuples).
        """
        if self.square_is_valid(square_original) is False:
            raise Exception("Piece.current_square not valid. Probably not initialyzed.")

        squares_inline = set()
        rank, file = square_original
        for i in range(1, 9):
            squares_inline.add((rank, i))
        for j in range(1, 9):
            squares_inline.add((j, file))
        squares_inline.remove(square_original)

        return squares_inline

    def get_squares_diago(self, square_original: Square_t):
        """Add all squares diagonally from the argument square to a set and
        returns it."""
        if self.square_is_valid(square_original) is False:
            raise Exception("Piece.current_square not valid. Probably not initialyzed.")

        rank, file = square_original
        squares_diago = set()
        # In sw
        i = 1
        while (rank - i) > 0 and (file - i) > 0:
            squares_diago.add((rank - i, file - i))
            i = i + 1

        # In nw
        i = 1
        while (rank + i) < 9 and (file - i) > 0:
            squares_diago.add((rank + i, file - i))
            i = i + 1

        # In se
        i = 1
        while (rank - i) > 0 and (file + i) < 9:
            squares_diago.add((rank - i, file + i))
            i = i + 1

        # In ne
        i = 1
        while (rank + i) < 9 and (file + i) < 9:
            squares_diago.add((rank + i, file + i))
            i = i + 1

        return squares_diago

    def get_squares_knight(self, square_origin: Square_t) -> set[Square_t]:
        """
        Return a set of tuples with squares a knight could jump to from
        original square.
        """
        if self.square_is_valid(square_origin) is False:
            raise Exception("Piece.current_square not valid. Probably not initialyzed.")
        moves = set()
        rank, file = square_origin
        operations = [
            (-1, -2),
            (-2, -1),
            (-1, 2),
            (-2, 1),
            (1, -2),
            (2, -1),
            (1, 2),
            (2, 1),
        ]
        for op in operations:
            i, j = op
            ri = rank + i
            fj = file + j
            if (0 < ri and ri < 9) and (0 < fj and fj < 9):
                moves.add((ri, fj))

        return moves


class Pawn(Piece):
    """Pawn only move straight forward by one square. Starting from the
    initial sqaure they have an additional opportunity to move two squares
    forward."""

    def __repr__(self):
        return f"Pawn {self.id}"

    def __str__(self):
        return f"square: {self.current_square}"

    def move_1_diago_forward(self, square_origin: Square_t) -> set[Square_t]:
        s = set()
        i, j = square_origin
        if self.color == "w":
            s.add(self.move_x_in_y(square_origin, 1, "nw"))
            s.add(self.move_x_in_y(square_origin, 1, "ne"))
        else:
            s.add(self.move_x_in_y(square_origin, 1, "sw"))
            s.add(self.move_x_in_y(square_origin, 1, "se"))
        return s

    def get_moves(self) -> set[Square_t]:
        moves = set()
        moves.add(self.move_x_up(self.current_square, 1))
        moves.add(self.move_x_up(self.current_square, 2))
        diago_forward_by_1 = self.move_1_diago_forward(self.current_square)
        tmp = moves.union(diago_forward_by_1)
        result = set()
        for sq in tmp:
            if self.square_is_valid(sq):
                result.add(sq)
        return result

    # TODO: promotion


class King(Piece):
    """King piece has the most restrictions. It can move in all directions by
    one square. But it can not move on a square where it would be threatened.
    """

    def __repr__(self):
        return f"King {self.id}"

    def get_moves(self) -> set[Square_t]:
        moves = set()
        directions = ["n", "s", "e", "w", "ne", "nw", "se", "sw"]
        for direct in directions:
            candidate = self.move_x_in_y(self.current_square, 1, direct)
            if self.square_is_valid(candidate):
                moves.add(candidate)

        return moves


class Queen(Piece):
    def __repr__(self):
        return f"Queen {self.id}"

    def get_moves(self) -> set[Square_t]:
        squares_straights = self.get_squares_straight(self.current_square)
        squares_diago = self.get_squares_diago(self.current_square)
        moves = squares_diago.union(squares_straights)
        return moves


class Bishop(Piece):
    def __repr__(self):
        return f"Bishop {self.id}"

    def get_moves(self):
        return self.get_squares_diago(self.current_square)


class Knight(Piece):
    def __repr__(self):
        return f"Knight {self.id}"

    def get_moves(self) -> set[Square_t]:
        return self.get_squares_knight(self.current_square)


class Rook(Piece):
    def __repr__(self):
        return f"Rook {self.id}"

    def get_moves(self) -> set[Square_t]:
        return self.get_squares_straight(self.current_square)
        return self.get_squares_straight(self.current_square)
