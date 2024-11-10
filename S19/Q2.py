def print_solution(board):
    """Function to print the solution of the board"""
    for row in board:
        print(" ".join(["Q" if x else "." for x in row]))
    print()

def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]"""
    # Check the column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check the left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, 4)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, row):
    """Try to solve the N-Queens problem recursively"""
    if row >= 4:
        print_solution(board)
        return True

    # Try placing a queen in each column of the current row
    for col in range(4):
        if is_safe(board, row, col):
            board[row][col] = 1  # Place the queen
            if solve_n_queens(board, row + 1):  # Recur to place the next queen
                return True
            board[row][col] = 0  # Backtrack if no valid solution is found
    
    return False

def solve_4_queens():
    """Solve the 4-Queens problem"""
    board = [[0 for _ in range(4)] for _ in range(4)]  # 4x4 chessboard initialized to 0
    if not solve_n_queens(board, 0):
        print("No solution exists")

# Run the 4-Queens solver
solve_4_queens()
