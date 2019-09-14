# project from https://medium.com/@andreasstckl/writing-a-chess-program-in-one-day-30daff4610ec

# import
import chess_project_1_definitions
import chess
import chess.svg
from IPython.display import SVG

# main script

board = chess.Board()
SVG(chess.svg.board(board=board,size=800))
