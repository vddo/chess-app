from CGames import Board, Position


def test_init_position():
    pos = Position(0)
    assert pos.move == 0
    assert len(pos.position.keys()) == 64
