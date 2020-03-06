from tkinter import *
from sudoku_backtracking import *
import time


class BuildProgram(object):
    def __init__(self, master):
        self.master = master

        self.board = [[0, 0, 0, 0, 0, 0, 9, 0, 0],
                      [0, 0, 9, 0, 4, 3, 0, 8, 0],
                      [3, 0, 0, 7, 0, 1, 0, 0, 0],
                      [0, 0, 0, 0, 8, 0, 0, 0, 9],
                      [0, 0, 5, 0, 0, 0, 0, 6, 0],
                      [4, 6, 0, 0, 0, 0, 5, 0, 0],
                      [0, 0, 8, 6, 0, 0, 0, 4, 0],
                      [0, 5, 0, 0, 7, 0, 0, 0, 0],
                      [0, 4, 0, 1, 5, 0, 7, 2, 0]]

        self.squares = [[0]*9 for _ in range(9)]

        def createSquares(board):
            for i in range(9):
                for j in range(9):
                    if self.board[i][j] == 0:
                        self.squares[i][j] = Label(root, text="", font='Times 20 bold', bg='white', fg='#344860', height=2, width=5)
                    else:
                        self.squares[i][j] = Label(root, text=str(board[i][j]), font='Times 20 bold', bg='white', fg='#344860', height=2, width=5)
                    self.squares[i][j].grid(sticky=W, row=i, column=j, padx=1, pady=1)


        def updateSquares(i, j, board):
            self.squares[i][j].config(text=str(board[i][j]))


        def deleteSpace(i, j, board):
            self.squares[i][j].config(text="")


        def updateSquaresFake(board):
            for i in range(9):
                for j in range(9):
                    self.squares[i][j].config(text=str(board[i][j]))


        def solve_sudoku(board):
            row, col = lookForSpace(board)
            if row == None:
                updateSquares(0, 0, board)
                return True
            for k in range(1, size+1):
                if isCorrectlyPlaced(row, col, k, board):
                    board[row][col] = k
                    time.sleep(0.001)
                    updateSquares(row, col, board)
                    self.master .update()
                    if solve_sudoku(board):
                        return True
                    board[row][col] = 0
                    deleteSpace(row, col, board)
            return False

        createSquares(self.board)

        self.btn = Button(master, text="Solve", command=lambda:solve_sudoku(self.board))
        self.btn.grid(sticky=W, row=9, column=0, columnspan=9, padx=238)


if __name__ == '__main__':
    def on_closing(master):
        print("Good bye")
        master.destroy()

    root = Tk()
    BuildProgram(root)
    root.configure(background='#344860')
    root.protocol("WM_DELETE_WINDOW", lambda:on_closing(root))
    root.mainloop()
