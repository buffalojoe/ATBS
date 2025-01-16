# keys() returns keys of a dictionary as a list
# values() returns values of a dictionary as a list
# items() returns key value pairs of a dictionary as a list of tuples
# get() return the value when provided a key. Returns the second value if the key is not found

board = {
    '1a': 'wking',
    '2a': 'bking',
}

#print(list(board.values()).count('wking'))

def isValidChessBoard(chess):
     
    validPieceCount = {
        'wking': 1,
        'wqueen': 1,
        'wrook': 2,
        'wbishop': 2,
        'wknight': 2,
        'wpawn': 8,
        'bking': 1,
        'bqueen': 1,
        'brook': 2,
        'bbishop': 2,
        'bknight': 2,
        'bpawn': 8
    }

    validSpaces = [
        '1a', '2a', '3a', '4a', '5a', '6a', '7a', '8a',
        '1b', '2b', '3b', '4b', '5b', '6b', '7b', '8b',
        '1c', '2c', '3c', '4c', '5c', '6c', '7c', '8c',
        '1d', '2d', '3d', '4d', '5d', '6d', '7d', '8d',
        '1e', '2e', '3e', '4e', '5e', '6e', '7e', '8e',
        '1f', '2f', '3f', '4f', '5f', '6f', '7f', '8f',
        '1g', '2g', '3g', '4g', '5g', '6g', '7g', '8g',
        '1h', '2h', '3h', '4h', '5h', '6h', '7h', '8h', 
    ]

    if list(chess.values()).count('bking') != validPieceCount.get('bking') or list(chess.values()).count('wking') != validPieceCount.get('wking'):
        return False

    if list(chess.values()).count('bqueen') > validPieceCount.get('bqueen') or list(chess.values()).count('wqueen') > validPieceCount.get('wqueen'):
        return False

    if list(chess.values()).count('brook') > validPieceCount.get('brook') or list(chess.values()).count('wrook') > validPieceCount.get('wrook'):
        return False

    if list(chess.values()).count('bbishop') > validPieceCount.get('bbishop') or list(chess.values()).count('wbishop') > validPieceCount.get('wbishop'):
        return False

    if list(chess.values()).count('bknight') > validPieceCount.get('bknight') or list(chess.values()).count('wknight') > validPieceCount.get('wknight'):
        return False

    if list(chess.values()).count('bpawn') > validPieceCount.get('bpawn') or list(chess.values()).count('wpawn') > validPieceCount.get('wpawn'):
        return False

    for item in list(chess.keys()):
        if item not in validSpaces:
            return False
    
    return True

print(isValidChessBoard(board))