# Function to print the board
def print_board(board):
    for row in board:
        print(' '.join('Q' if x == 1 else '.' for x in row))
    print()

# Function to check if it's safe to place a queen at board[row][col]
def is_safe(board, row, col):
    # Check this column on all previous rows
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, len(board))):
        if board[i][j] == 1:
            return False
    
    return True

# Backtracking function to solve the problem
def solve_queens(board, row):
    # If all queens are placed, return True
    if row == len(board):
        return True
    
    # Try all columns in the current row
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1  # Place the queen
            
            # Recursively place queens in the next row
            if solve_queens(board, row + 1):
                return True
            
            # Backtrack: Remove the queen
            board[row][col] = 0
    
    # If no column is valid for the current row, return False
    return False

# Function to initiate the 4-Queens problem solution
def four_queens():
    size = 4  # 4x4 board
    board = [[0 for _ in range(size)] for _ in range(size)]
    
    if solve_queens(board, 0):
        print("Solution found:")
        print_board(board)
    else:
        print("No solution exists.")

# Run the 4-Queens solver
four_queens()
