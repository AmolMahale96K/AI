def print_board(board, n):
    """Print the board."""
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

def is_safe(board, row, col, n):
    """Check if placing a queen at (row, col) is safe."""
    # Check this column on all previous rows
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens(board, row, n):
    """Try to place queens row by row."""
    # If all queens are placed, return True
    if row == n:
        return True
    
    # Try all columns in the current row
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place the queen
            
            # Recur to place the next queen
            if solve_n_queens(board, row + 1, n):
                return True
            
            # Backtrack
            board[row][col] = 0
    
    return False  # No solution found

def n_queens(n):
    """Solve the N-Queens problem."""
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    if solve_n_queens(board, 0, n):
        print("Solution found:")
        print_board(board, n)
    else:
        print("No solution exists.")

# Input the size of the board (N)
n = int(input("Enter the size of the board (N): "))

# Solve the N-Queens problem
n_queens(n)
