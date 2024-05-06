24-05-07


## TODOS
- implement get_moves for the rest of the pieces
- implement get_moves_inline for Queen and Rook



24-05-05

## DO NEXT

## TODOS

- [] implement init_start_position()
  - delete all piece instances
  - init full set of pieces for both colors
  - for all pieces call method go_to_square(home_square)

## WORKED ON

### Initialze home position on Board

The board needs the method init_home_position() to set up the start for a chess game. Things that need to be prepared:

- Piece subclasses need a class attribute home_squares; simply hard coded
