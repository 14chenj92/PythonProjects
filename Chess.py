import chess
import chess.engine

# Initialize the board
board = chess.Board()

# Function to print the board
def print_board():
    print(board)

# Function to make a move
def make_move(move):
    try:
        board.push_san(move)
    except ValueError:
        print("Invalid move. Please try again.")
        return False
    return True

# Main game loop
def main():
    print("Welcome to Python Chess!")
    print_board()
    while not board.is_game_over():
        if board.turn == chess.WHITE:
            print("\nWhite to move")
        else:
            print("\nBlack to move")
        
        move = input("Enter your move (in standard algebraic notation): ")
        if move.lower() == 'quit':
            print("Game terminated.")
            break
        if make_move(move):
            print_board()
        else:
            continue

    print("Game over!")
    result = board.result()
    print("Result: " + result)

if __name__ == "__main__":
    main()
