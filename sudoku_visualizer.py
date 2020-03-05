from tkinter import *
from sudoku_backtracking import *
import time

class BuildProgram(object):
    def __init__(self, master):
        self.master = master

        self.board = [[0, 0, 8, 1, 0, 0, 5, 9, 2],
        [5, 0, 9, 0, 0, 0, 1, 8, 0],
        [0, 0, 2, 8, 0, 5, 3, 4, 6],
        [0, 0, 5, 0, 0, 0, 8, 7, 4],
        [8, 0, 0, 0, 5, 0, 2, 0, 1],
        [1, 0, 6, 0, 0, 0, 9, 0, 0],
        [0, 0, 7, 2, 1, 6, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 1, 0],
        [6, 0, 1, 0, 4, 3, 7, 0, 0]]

        self.squares = [[0]*9 for _ in range(9)]

        def createSquares(board):
            for i in range(9):
                for j in range(9):
                    if self.board[i][j] == 0:
                        self.squares[i][j] = Label(root, text="", font='Times 20 bold', bg='gray', fg='red', height=2, width=5)
                    else:
                        self.squares[i][j] = Label(root, text=str(board[i][j]), font='Times 20 bold', bg='gray', fg='red', height=2, width=5)
                    self.squares[i][j].grid(sticky=W, row=i, column=j, padx=1, pady=1)


        def updateSquares(board):
            print("updating")
            self.squares[i][j].config(text=str(board[i][j]))
            time.sleep(0.5)


        def updateSquaresFake(board):
            for i in range(9):
                for j in range(9):
                    self.squares[i][j].config(text=str(board[i][j]))


        def solve_sudoku(board):
            row, col = lookForSpace(board)
            if row == None:
                updateSquaresFake(board)
                return True
            for k in range(1, size+1):
                if isCorrectlyPlaced(row, col, k, board):
                    board[row][col] = k
                    #updateSquares(row, col, board)
                    if solve_sudoku(board):
                        return True
                    board[row][col] = 0
            return False

        createSquares(self.board)

        self.btn = Button(master, text="Solve", command=lambda:solve_sudoku(self.board))
        self.btn.grid(sticky=W, row=9, column=0, columnspan=9, padx=238)


if __name__ == '__main__':
    root = Tk()
    BuildProgram(root)
    root.mainloop()
