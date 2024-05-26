from CGames import Board, Position


def test_init_position():
    pos = Position(0)
    pos2 = Position(1, pos)
    assert pos.move == 0
    assert len(pos.position.keys()) == 64
    assert pos2.ancestor == pos


if __name__ == "__main__":
    pos = Position(0)
