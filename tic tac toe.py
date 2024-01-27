def print_board(board):
    # چاپ تخته بازی
    for row in board:
        print(" ".join(row))

def check_winner(board, player):
    # بررسی برنده بودن بازیکن
    for i in range(3):
        # بررسی خطوط افقی و عمودی
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    # بررسی قطرها
    return all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3))

def is_board_full(board):
    # بررسی پر بودن تخته بازی
    return all(cell != " " for row in board for cell in row)

def make_move(board, player):
    try:
        # درخواست ورود مختصات از بازیکن
        row, col = map(int, input(f"Player {player}, enter row and column (0, 1, or 2) separated by space: ").split())
        # بررسی صحت حرکت و انجام آن
        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            board[row][col] = player
            return True
        else:
            print("Invalid move")
            return make_move(board, player)
    except ValueError:
        print("Invalid input")
        return make_move(board, player)

def play_game(board, players, current_player):
    # چاپ وضعیت فعلی تخته بازی
    print_board(board)
    
    # انجام حرکت بازیکن و بررسی وضعیت بازی
    if make_move(board, current_player):
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins")
        elif is_board_full(board):
            print_board(board)
            print("draw")
        else:
            # تغییر نوبت بازیکن
            play_game(board, players, players[1] if current_player == players[0] else players[0])

if __name__ == "__main__":
    # ایجاد تخته بازی
    board = [[" "]*3 for _ in range(3)]
    # تعیین بازیکن‌ها
    players = ["X", "O"]
    # تعیین بازیکن فعلی
    current_player = players[0]

    # شروع بازی
    play_game(board, players, current_player)
