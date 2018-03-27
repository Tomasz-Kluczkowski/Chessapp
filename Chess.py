board = [[1] * 8 for i in range(8)]

def knight_moves(position, board):
    """This function shows all possible knight moves - assuming nothing else
    is on the board"""

    column, row = position
    row = int(row) - 1
    column = ord(column) - ord('a')
    i, j = row, column
    possible_moves = []

    try:
        move = board[i + 2][j + 1]
        possible_moves.append([i + 2, j + 1])
    except:
        pass
    try:
        move = board[i + 2][j - 1]
        possible_moves.append([i + 2, j - 1])
    except:
        pass
    try:
        move = board[i + 1][j - 2]
        possible_moves.append([i + 1, j - 2])
    except:
        pass
    try:
        move = board[i + 1][j + 2]
        possible_moves.append([i + 1, j + 2])
    except:
        pass
    try:
        move = board[i - 1][j - 2]
        possible_moves.append([i - 1, j - 2])
    except:
        pass
    try:
        move = board[i - 1][j + 2]
        possible_moves.append([i - 1, j + 2])
    except:
        pass
    try:
        move = board[i - 2][j - 1]
        possible_moves.append([i - 2, j - 1])
    except:
        pass
    try:
        move = board[i - 2][j + 1]
        possible_moves.append([i - 2, j + 1])
    except:
        pass
    return possible_moves

position = 'a4'
print(knight_moves(position, board))
