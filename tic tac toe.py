def print_board(board):
    for row in board:
        print(" ".join(row))

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    return all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3))

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def make_move(board, player):
    try:
        row, col = map(int, input(f"Player {player}, enter row and column (0, 1, or 2) separated by space: ").split())
        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            board[row][col] = player
            return True
        else:
            print("Invalid move. Try again.")
            return make_move(board, player)
    except ValueError:
        print("Invalid input. Please enter two numbers separated by space.")
        return make_move(board, player)

def play_game(board, players, current_player):
    print_board(board)
    if make_move(board, current_player):
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
        else:
            play_game(board, players, players[1] if current_player == players[0] else players[0])

if __name__ == "__main__":
    board = [[" "]*3 for _ in range(3)]
    players = ["X", "O"]
    current_player = players[0]

    play_game(board, players, current_player)