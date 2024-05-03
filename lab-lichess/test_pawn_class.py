import CGames
import pytest

# In chess you say (line, rank) like a2
# coordinates are implemented [i,j] <- (rank, line)
coord_a2 = [2, 1]
coord_e7 = [7, 5]

# Initialize pawn
pawn_w = CGames.Pawn()
pawn_w.init_color('w')
pawn_w.init_pos_coord(coord_a2)

# Init King
king = CGames.King()
king.init_pos_coord(coord_a2)

pawn_b = CGames.Pawn()
pawn_b.init_color('b')
pawn_b.init_pos_coord(coord_e7)

pawn_error = CGames.Pawn()


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
        king.move_x_in_y(king.pos_coordinates, 1, 'ne'),
        king.move_x_in_y([1, 5], 1, 'n'),
        king.move_x_in_y([8, 5], 1, 's'),
        king.move_x_in_y([1, 1], 1, 'nw'),
        king.move_x_in_y([1, 8], 1, 'se'),
        king.move_x_in_y([6, 5], 1, 'w'),
        king.move_x_in_y([4, 5], 1, 'e')
    )


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
    assert king.pos_coordinates == coord_a2
    assert k_moves() == ((3, 2), (2, 5), (7, 5), (2, 0), (0, 9), (6, 4), (4, 6))



if __name__ == '__main__':
    k_moves()
