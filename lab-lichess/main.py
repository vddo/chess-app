import CGames
from icecream import ic

def main():
    ic('Hello')

if __name__ == '__main__':
    pawn = CGames.Pawn()
    pawn.init_color('w')
    ic(pawn.move_1_up([2, 1]))
