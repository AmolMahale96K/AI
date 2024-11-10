import math

# Board representation
# 0 - empty, 1 - player X, -1 - player O

def is_winner(board, player):
    """Check if a player has won"""
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def is_full(board):
    """Check if the board is full"""
    return all(board[i][j] != 0 for i in range(3) for j in range(3))

def evaluate(board):
    """Evaluate the board: 10 for X win, -10 for O win, 0 for draw"""
    if is_winner(board, 1):
        return 10
    if is_winner(board, -1):
        return -10
    return 0

def minimax(board, depth, is_max):
    """Minimax algorithm"""
    score = evaluate(board)

    # If Maximizer (X) wins
    if score == 10:
        return score - depth

    # If Minimizer (O) wins
    if score == -10:
        return score + depth

    # If board is full, it's a draw
    if is_full(board):
        return 0

    if is_max:
        best = -math.inf
        # Try all possible moves for the maximizer (X)
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 1  # Make the move
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = 0  # Undo the move
        return best

    else:
        best = math.inf
        # Try all possible moves for the minimizer (O)
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = -1  # Make the move
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = 0  # Undo the move
        return best

def find_best_move(board):
    """Find the best move for the current player (X)"""
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = 1  # Make the move
                move_val = minimax(board, 0, False)
                board[i][j] = 0  # Undo the move

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

# Tic-Tac-Toe Board
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Run the Mini-Max algorithm to find the best move for X
best_move = find_best_move(board)
print(f"Best move for X is at row {best_move[0]} and column {best_move[1]}")
