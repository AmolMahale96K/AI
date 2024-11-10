import random

# Print the current board state
def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 5)

# Check if a player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in range(3):
        if all([cell == player for cell in board[row]]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

# Check if the board is full
def is_full(board):
    return all([cell != ' ' for row in board for cell in row])

# Minimax algorithm for the computer's best move
def minimax(board, depth, is_maximizing):
    if check_winner(board, 'X'):
        return 1  # 'X' wins
    if check_winner(board, 'O'):
        return -1  # 'O' wins
    if is_full(board):
        return 0  # Draw

    if is_maximizing:
        best = -float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    best = max(best, minimax(board, depth + 1, False))
                    board[row][col] = ' '
        return best
    else:
        best = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'O'
                    best = min(best, minimax(board, depth + 1, True))
                    board[row][col] = ' '
        return best

# Find the best move for the computer
def best_move(board):
    best_val = -float('inf')
    move = (-1, -1)
    
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'X'
                move_val = minimax(board, 0, False)
                board[row][col] = ' '
                if move_val > best_val:
                    best_val = move_val
                    move = (row, col)
    
    return move

# Main function to play the game
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    
    while True:
        print_board(board)
        
        # Player 'O' (Human)
        row, col = map(int, input("Enter your move (row col): ").split())
        if board[row][col] == ' ':
            board[row][col] = 'O'
        else:
            print("Invalid move, try again!")
            continue

        if check_winner(board, 'O'):
            print_board(board)
            print("Player 'O' wins!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Player 'X' (AI - Minimax)
        print("Computer's move:")
        move = best_move(board)
        board[move[0]][move[1]] = 'X'

        if check_winner(board, 'X'):
            print_board(board)
            print("Computer (Player 'X') wins!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a draw!")
            break

# Run the game
if __name__ == "__main__":
    play_game()
