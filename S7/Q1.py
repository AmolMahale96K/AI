import math

# Constants
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = " "

# Function to check if the game is over
def is_game_over(board):
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return True
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return True
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return True
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return True
    # Check for a draw (if there are no empty spaces left)
    if all(board[i][j] != EMPTY for i in range(3) for j in range(3)):
        return "Draw"
    return False

# Minimax function with alpha-beta pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    result = is_game_over(board)
    if result == PLAYER_X:
        return -1
    if result == PLAYER_O:
        return 1
    if result == "Draw":
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    score = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = EMPTY
                    best_score = max(best_score, score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    score = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = EMPTY
                    best_score = min(best_score, score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score

# Function to find the best move for the AI
def find_best_move(board):
    best_move = None
    best_value = -math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_O
                move_value = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = EMPTY
                if move_value > best_value:
                    best_value = move_value
                    best_move = (i, j)
    return best_move

# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to play the game
def play_game():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    current_player = PLAYER_X  # Player X starts the game

    while True:
        print_board(board)
        if current_player == PLAYER_X:
            print("Player X's turn (Human):")
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER_X
                current_player = PLAYER_O
            else:
                print("Invalid move, try again.")
                continue
        else:
            print("Player O's turn (AI):")
            best_move = find_best_move(board)
            board[best_move[0]][best_move[1]] = PLAYER_O
            current_player = PLAYER_X
        
        result = is_game_over(board)
        if result:
            print_board(board)
            if result == "Draw":
                print("It's a draw!")
            else:
                print(f"{result} wins!")
            break

if __name__ == "__main__":
    play_game()
