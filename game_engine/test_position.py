from CGames import Board, Position, Piece
from icecream import ic

pos = Position(0)
pos2 = Position(1, pos)
b = Board()

b.init_board()
p = b.position


def get_piece(square: tuple[int, int]) -> Piece:
    id = p.position[square]
    return b.active_pieces[id]


def test_init_position():
    assert pos.move == 0
    assert len(pos.position.keys()) == 64
    assert pos2.ancestor == pos


def test_init_board():
    # TODO: get id from p.position[square]
    # get Piece instance from b.active_pieces[id]
    return


if __name__ == "__main__":
    pos = Position(0)
    b = Board()
    b.init_board()
    ic(isinstance(b, Board))
    ic(p.position)
    ic(b.active_pieces)
    # ic(get_piece((1, 1)))
