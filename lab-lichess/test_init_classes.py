import CGames
import pytest


# Initialize pawn
pawn_w = CGames.Pawn()
pawn_w.init_color('w')

pawn_b = CGames.Pawn()
pawn_b.init_color('b')

pawn_error = CGames.Pawn()

# In chess you say (line, rank) like a2
# coordinates are implemented [i,j] <- (rank, line)
coord_a2 = [2, 1]

def f_move_pawn_w_up():
    return pawn_w.move_1_up(coord_a2)

def f_move_pawn_b_up():
    return pawn_b.move_1_up(coord_a2)

def f_pawn_color_error():
    return pawn_error.init_color('red')


def test_move_up():
    assert f_move_pawn_w_up() == (3, 1)
    assert f_move_pawn_b_up() == (1, 1)

    with pytest.raises(ValueError):
        f_pawn_color_error()
