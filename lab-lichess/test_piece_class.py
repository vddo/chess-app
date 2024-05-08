import CGames
from icecream import ic
import pytest

# In chess you say (line, rank) like a2
# coordinates are implemented [i,j] <- (rank, line)
coord_a2 = [2, 1]
coord_e7 = [7, 5]

# Initialize pawn
pawn_w = CGames.Pawn('bd99')
pawn_w.init_color('w')
pawn_w.goto_square(coord_a2)

# Init King
king = CGames.King('jdje')
king.goto_square(coord_a2)

pawn_b = CGames.Pawn('jd83')
pawn_b.init_color('b')
pawn_b.goto_square(coord_e7)

pawn_error = CGames.Pawn('e23k')

queen = CGames.Queen('q1')
queen.init_color('w')
queen.goto_square((3, 2))

bish = CGames.Bishop('id')
bish.init_color('b')
bish.goto_square((4, 4))

rook = CGames.Rook('id')
rook.init_color('b')
rook.goto_square((8, 8))

# Init board
board = CGames.Board()


def f_move_pawn_w_up():
    return (pawn_w.move_1_up(coord_a2), pawn_w.move_x_up(coord_a2, 2))

def f_move_pawn_b_up():
    return (pawn_b.move_1_up(coord_e7), pawn_b.move_x_up(coord_e7, 2))

def f_pawn_color_error():
    return pawn_error.init_color('red')

def f_pawn_w_available_moves():
    pawn_w.get_moves()
    return pawn_w.avail_moves

def f_pawn_b_available_moves():
    pawn_b.get_moves()
    return pawn_b.avail_moves

def k_moves():
    return (
        king.move_x_in_y(king.current_square, 1, 'ne'),
        king.move_x_in_y([1, 5], 1, 'n'),
        king.move_x_in_y([8, 5], 1, 's'),
        king.move_x_in_y([1, 1], 1, 'nw'),
        king.move_x_in_y([1, 8], 1, 'se'),
        king.move_x_in_y([6, 5], 1, 'w'),
        king.move_x_in_y([4, 5], 1, 'e')
    )

def q_moves():
    queen_moves_og_32 = {
        (3, 1), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8),
        (1, 2), (2, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2),
        (2, 1), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7),
        (4, 1), (2, 3), (1, 4)
    }
    queen_moves = queen.get_moves()
    for sq in queen_moves:
        queen_moves_og_32.remove(sq)
    return queen_moves_og_32


def test_move_up():
    # Assert pawn movement
    assert f_move_pawn_w_up() == ((3, 1), (4, 1))
    assert f_move_pawn_b_up() == ((6, 5), (5, 5))

    # Color error
    with pytest.raises(ValueError):
        f_pawn_color_error()


    # Available pawn moves
    assert f_pawn_w_available_moves() == [(3, 1), (4, 1)]
    assert f_pawn_b_available_moves() == [(6, 5), (5, 5)]

    # init moves before init position
    with pytest.raises(ValueError):
        pawn_error.get_moves()

    # Assert king moves
    assert king.current_square == coord_a2
    assert k_moves() == ((3, 2), (2, 5), (7, 5), (2, 0), (0, 9), (6, 4), (4, 6))

def test_moves():
    assert pawn_b.to_boarder_straight((2, 5)) == [ (3, 'e'), (4, 'w'), (6, 'n'), (1, 's') ]
    assert pawn_b.get_squares_straight((2, 5)) == {
        (2, 1), (2, 2), (2, 3), (2, 4), (2, 6), (2, 7), (2, 8),
        (1, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5)
    }
    assert pawn_b.get_squares_diago((3, 4)) == {
        (1, 2), (1, 6), (2, 3), (2, 5), (4, 3), (4, 5),
        (5, 2), (5, 6), (6, 1), (6, 7), (7, 8)
    }

    q_moves_32 = q_moves()
    assert len( q_moves_32 ) == 0

    assert sorted(rook.get_moves()) ==  [
        (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8),
        (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7)
    ]

    assert sorted(bish.get_moves()) == [
        (1, 1), (1, 7), (2, 2), (2, 6), (3, 3), (3, 5),
        (5, 3), (5, 5), (6, 2), (6, 6), (7, 1), (7, 7), (8, 8)
    ]


if __name__ == '__main__':
    # sq = queen.get_moves()
    q1 = queen.get_squares_straight((3, 2))
    q2 = queen.get_squares_diago((3, 2))
    q3 = q1.union(q2)
    ic(q1, q2, '\n', q3)
