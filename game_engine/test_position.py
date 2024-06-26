import CGames as cg
from CGames import Board, Position, Piece, Square_t
from icecream import ic

# type Square_t = tuple[int, int]

pos = Position(0)
pos2 = Position(1, pos)
b = Board()

b.init_board()
p = b.position


def get_piece(square: Square_t) -> Piece:
    id = p.get_piece(square)
    return b.active_pieces[id]


def test_init_position():
    assert pos.halfturn == 0
    assert len(pos.position.keys()) == 64
    assert pos2.ancestor == pos


def test_init_board():
    rw1 = get_piece((1, 1))
    assert isinstance(rw1, cg.Rook) and rw1.color == "w"
    qw = get_piece((1, 4))
    assert isinstance(qw, cg.Queen) and qw.color == "w"
    pw1 = get_piece((2, 8))
    assert isinstance(pw1, cg.Pawn) and qw.color == "w"
    nw1 = get_piece((1, 7))
    assert isinstance(nw1, cg.Knight) and qw.color == "w"

    rb1 = get_piece((8, 8))
    assert isinstance(rb1, cg.Rook) and rb1.color == "b"
    kb = get_piece((8, 5))
    assert isinstance(kb, cg.King) and kb.color == "b"
    pb1 = get_piece((7, 3))
    assert isinstance(pb1, cg.Pawn) and pb1.color == "b"
    bb1 = get_piece((8, 3))
    assert isinstance(bb1, cg.Bishop) and bb1.color == "b"
    return


def test_inherit_position():
    p1_inherit_p = Position(1, p)
    assert p1_inherit_p.position == p.position


if __name__ == "__main__":
    pos = Position(0)
    ic(isinstance(b, Board))
    ic(get_piece((1, 1)))
    ic(isinstance(get_piece((1, 1)), cg.Rook))
