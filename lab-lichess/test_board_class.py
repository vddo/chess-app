import CGames
from CGames import Board
from icecream import ic
import pytest


# Init board
b = Board()

# functions
def b_init_piece():
    b.init_piece('k', 1, 'b', 'king1')
    tmp = list(b.active_pieces.keys())
    return(tmp[0], b.active_pieces[tmp[0]])

def test_init():
    assert b_init_piece() == ('king1', None)
