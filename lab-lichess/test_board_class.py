import CGames
from CGames import Board
from icecream import ic
import pytest

def generate_homesquares():
    s = set()
    rows = [1, 2, 7, 8]
    for i in rows:
        for j in range(8):
            s.add(( i, j ))

    return s

# Init board
b = Board()

# functions
def b_init_piece():
    b.init_piece('k', 'b', 'king1')
    tmp = list(b.active_pieces.keys())
    return repr(b.active_pieces[tmp[0]])

def test_init():
    assert b_init_piece() == ('King king1')

# Test init board
def test_init_board():
    b.init_board()
    l_pieces = list(b.active_pieces.keys())
    assert len(l_pieces) == 18

    s = generate_homesquares()
    for elem in l_pieces:
        s.remove(b.active_pieces[elem].current_square)
    assert len(l_pieces) == 0




if __name__ == '__main__':
    s = generate_homesquares()
    print(s)
    b.init_board()
    l_pieces = list(b.active_pieces.keys())
    print(l_pieces)
