# Define the Tic-Tac-Toe board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Function to print the board
def print_board():
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check if a player has won
def check_winner():
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    
    # No winner yet
    return None

# Function to check if the board is full (draw condition)
def is_draw():
    for row in board:
        if ' ' in row:
            return False
    return True

# Function to play the game
def play_game():
    current_player = 'X'  # Player X starts first
    while True:
        print_board()
        print(f"Player {current_player}'s turn:")
        
        # Input move
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != ' ':
                print("Invalid move. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter integers between 0 and 2.")
            continue
        
        # Place the move on the board
        board[row][col] = current_player
        
        # Check for winner
        winner = check_winner()
        if winner:
            print_board()
            print(f"Player {winner} wins!")
            break
        
        # Check for draw
        if is_draw():
            print_board()
            print("It's a draw!")
            break
        
        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()
