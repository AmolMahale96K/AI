# Function to print the chessboard
def print_board(board):
    for row in board:
        print(' '.join('Q' if cell else '.' for cell in row))
    print()

# Function to check if a queen can be safely placed at board[row][col]
def is_safe(board, row, col, n):
    # Check this column on all rows before this row
    for i in range(row):
        if board[i][col]:
            return False
    
    # Check upper left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j]:
            return False
    
    # Check upper right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j]:
            return False
    
    return True

# Backtracking function to solve the N-Queens problem
def solve_n_queens(board, row, n):
    # If all queens are placed, return True
    if row >= n:
        return True
    
    # Try placing the queen in all columns for this row
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = True  # Place the queen
            
            # Recur to place the next queen
            if solve_n_queens(board, row + 1, n):
                return True
            
            # If placing queen in (row, col) doesn't lead to a solution, backtrack
            board[row][col] = False
    
    return False  # No solution found

# Function to solve the 8-Queens problem
def eight_queens():
    n = 8  # 8x8 board
    board = [[False for _ in range(n)] for _ in range(n)]
    
    if solve_n_queens(board, 0, n):
        print("Solution found:")
        print_board(board)
    else:
        print("No solution exists.")

# Run the 8-Queens solver
if __name__ == "__main__":
    eight_queens()

