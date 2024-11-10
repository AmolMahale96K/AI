def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens(board, row, n):
    # If all queens are placed
    if row == n:
        # Print the board
        print_board(board, n)
        return True
    
    res = False
    # Try placing the queen in each column of the current row
    for col in range(n):
        if is_safe(board, row, col, n):
            # Place the queen
            board[row] = col
            # Recur to place the rest of the queens
            res = solve_n_queens(board, row + 1, n) or res
            # Backtrack (remove the queen)
            board[row] = -1
    return res

def print_board(board, n):
    """Function to print the chessboard configuration"""
    for i in range(n):
        row = ['Q' if board[i] == j else '.' for j in range(n)]
        print(" ".join(row))
    print()

def n_queens(n):
    # Initialize the board (one element per row, column not assigned yet)
    board = [-1] * n
    if not solve_n_queens(board, 0, n):
        print("No solution found.")

# Example: Solve the 4-Queens problem
n_queens(4)
