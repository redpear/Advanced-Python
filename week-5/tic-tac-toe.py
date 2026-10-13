import numpy as np


def show_board(board):
    print('\n  0   1   2')
    for i in range(3):
        print(i, ' | '.join(board[i]))
        if i < 2:
            print('  ---------')
    print()


def check_winner(board, player):
    for i in range(3):
        if np.all(board[i, :] == player):
            return True
        if np.all(board[:, i] == player):
            return True
    if np.all(np.diag(board) == player):
        return True
    if np.all(np.diag(np.fliplr(board)) == player):
        return True
    return False


def play_game():
    board = np.full((3, 3), ' ', dtype='<U1')
    player = 'X'
    print('Welcome to Tic-Tac-Toe!')
    print('Enter row and column numbers from 0 to 2.')
    show_board(board)

    while True:
        print('Player', player, 'turn')
        try:
            row = int(input('Enter row (0-2): '))
            col = int(input('Enter column (0-2): '))
        except ValueError:
            print('Please enter whole numbers only.\n')
            continue

        if row < 0 or row > 2 or col < 0 or col > 2:
            print('That position is outside the board. Try again.\n')
            continue
        if board[row, col] != ' ':
            print('That square is already taken. Try again.\n')
            continue

        board[row, col] = player
        show_board(board)

        if check_winner(board, player):
            print('Player', player, 'wins!')
            break
        if np.all(board != ' '):
            print('The game is a draw!')
            break
        player = 'O' if player == 'X' else 'X'


if __name__ == '__main__':
    play_game()
