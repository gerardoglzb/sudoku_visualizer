from math import sqrt
size = 9 #Size of sudoku (9)
sqrt_size = int(sqrt(size))

board = [[0, 0, 8, 1, 0, 0, 5, 9, 2],
        [5, 0, 9, 0, 0, 0, 1, 8, 0],
        [0, 0, 2, 8, 0, 5, 3, 4, 6],
        [0, 0, 5, 0, 0, 0, 8, 7, 4],
        [8, 0, 0, 0, 5, 0, 2, 0, 1],
        [1, 0, 6, 0, 0, 0, 9, 0, 0],
        [0, 0, 7, 2, 1, 6, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 1, 0],
        [6, 0, 1, 0, 4, 3, 7, 0, 0]]


# Checks if you can put a number in a certain place in the board.
def isCorrectlyPlaced(a, b, n, board):
    for i in range(size):
        if board[a][i] == n: # Checks for the number we're placing on the same line.
            return False
        if board[i][b] == n: # Checks for the number we're placing on the column.
            return False
    vertical_square = a // sqrt_size
    horizontal_square = b // sqrt_size
    # Checks for the number we're placing on its 3x3 square.
    for i in range(sqrt_size*vertical_square, sqrt_size*vertical_square + sqrt_size):
        for j in range(sqrt_size*horizontal_square, sqrt_size*horizontal_square + sqrt_size):
            if board[i][j] == n:
                return False
    return True


# Looks for a space with a 0 in it.
def lookForSpace(board):
    for x in range(size):
        for y in range(size):
            if board[x][y] == 0:
                return x, y
    return None, None


# Prints the board.
def print_board(board):
    print("\n---------------------------\n")
    for square in board:
        print(square)


def sudoku_backtrack(board):
    row, col = lookForSpace(board)
    if row == None: # When there are no empty spaces, we're done.
        return True
    for k in range(1, size+1): # Tries to place all 9 possible numbers.
        if isCorrectlyPlaced(row, col, k, board):
            board[row][col] = k # Places the number.
            if sudoku_backtrack(board): # Recursion.
                return True
            board[row][col] = 0 # If a mistake is made, we empty the space again.
    return False

sudoku_backtrack(board)
