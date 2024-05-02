"""Working on a rudimentary implementation of a Chess Board Game"""

class CGame:
    def __init__(self):
        self.current_board = None
        self.winner = None
        self.time_control = 'blitz'
        self.turn_count = 0
        self.board_history = []
        self.players_turn = 'white'


class Board:
    def __init__(self):
        self.players_turn = 'white'
        self.estimation = 0.0
        self.all_available_moves = []
        self.position = []


class Piece:
    def __init__(self):
        self.color = None
        self.pos_coordinates = None
        self.available_moves = []


    # [i, j] <- [ranks, lines]
    def move_1_up(self, start: list[int, int]):
        i, j = start
        if self.color == 'w':
            return (i+1, j)

        return (i-1, j)

    # def move_x_up(self, start: list[int, int], x: int):
        

            

        
        

class Pawn(Piece):
    def init_color(self, col):
        if col in ('w', 'b'):
            self.color = col
        else:
            raise ValueError('Color invalid')


    def init_pos_coord(self, coord):
        self.pos_coordinates = coord


    def init_avail_moves(self):
        self.available_moves = []

