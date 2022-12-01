from dokusan import generators
import numpy as np

board = list(str(generators.random_sudoku(avg_rank = 100)))


with open("board.txt", "w") as f:
    b = """"""
    b+="".join(board)
    b+="\n\n"
    for i in range(9): 
        b += " ".join(board[i*9:(1+i)*9])
        b+= "\n"
    f.write(b)