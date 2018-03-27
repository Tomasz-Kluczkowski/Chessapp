board = [[1] * 8 for i in range(8)]

possible_moves = []

def knight_moves(position, board):
    """This function shows all possible knight moves - assuming nothing else
    is on the board"""

    column, row = position
    row = int(row) - 1
    column = ord(column) - ord('a')
    i, j = row, column
    
    addMove(i, j, 2, 1)
    addMove(i, j, 2, -1)
    addMove(i, j, 1, -2)
    addMove(i, j, 1, 2)
    addMove(i, j, -1, -2)
    addMove(i, j, -1, 2)
    addMove(i, j, -2, -1)
    addMove(i, j, -2, 1)
    return possible_moves


def addMove(row, col, diff_row, diff_col):
    if row+diff_row>=0 and col+diff_col>=0: 
        possible_moves.append([row + diff_row, col + diff_col])
    
    
position = 'a4'
print(knight_moves(position, board))
