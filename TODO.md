# v0.0.1

## TODO

- [x] while init board place all pieces on sqare in position
- [x] pass position from ancestor
- [ ] implement class Move
- [ ] implement Board is valid move

### New class Move
A class that models a piece move. 
Fields: square, piece id
Needs to generate move notation?

Note:
An advanced feature is it to do proper notation like if more than one piece can reach a square an alternative notation is used.

Intruduce a new class 'Position'. Each instances will have the attributes:

- turn or move ... can derive from 'Board's turn; starts with 0 and initial 
position; uneven moves was white; 

- positioning ... [dict] that maps piece id's to sqares; will be needed to check valid moves 
and captures

- ancestor ... which 'Position' came before; arrow head leading to position from where 
the current position derived from

## positioning

methods:
- init_positioning... init sqares as keys and put all pieces to there home squares
- inherit_positioning... call passon_pos from ancestor and take over position
- passon_pos... return the position
- set_piece... takes piece id and put in positioning 
- get_piece...



24-05-08

## TODOS

- implement check if move is valid
- check if move take another piece

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
