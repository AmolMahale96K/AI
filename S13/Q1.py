import math

# Check if the board is full
def is_full(board):
    return all([cell != ' ' for row in board for cell in row])

# Check if a player has won the game
def is_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

# Evaluate the board and return score
def evaluate(board):
    if is_winner(board, 'X'):
        return 1  # Maximizing player wins
    elif is_winner(board, 'O'):
        return -1  # Minimizing player wins
    return 0  # Draw or game ongoing

# Mini-Max Algorithm to find the optimal move
def minimax(board, depth, is_maximizing):
    score = evaluate(board)
    
    # If Maximizer or Minimizer has won, return score
    if score == 1 or score == -1:
        return score
    
    # If board is full (draw), return 0
    if is_full(board):
        return 0
    
    # Maximizing player ('X')
    if is_maximizing:
        best = -math.inf  # Initialize to a very small value
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = ' '  # Undo the move
        return best
    else:  # Minimizing player ('O')
        best = math.inf  # Initialize to a very large value
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = ' '  # Undo the move
        return best

# Function to find the best move
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)
    
    # Try every cell, evaluate minimax function and find the best move
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'  # Maximizing player's move
                move_val = minimax(board, 0, False)
                board[i][j] = ' '  # Undo the move
                
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)
    
    return best_move

# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("--------")

# Main function to play the game
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Tic-Tac-Toe Game!")
    print("Player 'X' is maximizing and Player 'O' is minimizing")
    
    while True:
        print_board(board)
        
        # Player 'X' move (AI)
        best_move = find_best_move(board)
        board[best_move[0]][best_move[1]] = 'X'
        
        if is_winner(board, 'X'):
            print_board(board)
            print("Player 'X' (AI) wins!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Player 'O' move (Human)
        print("Player 'O', your turn!")
        while True:
            try:
                row, col = map(int, input("Enter row and column (0-2) separated by space: ").split())
                if board[row][col] == ' ':
                    board[row][col] = 'O'
                    break
                else:
                    print("Cell already filled. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter valid row and column (0-2).")
        
        if is_winner(board, 'O'):
            print_board(board)
            print("Player 'O' wins!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a draw!")
            break

# Run the game
if __name__ == "__main__":
    play_game()
