## Solve the "Hardest" Sudoku Problem

##  Throughout this program:
##  A sodoku puzzle consists of 81 chars from digits 0-9 with 0 stands for an empty place, e.g. '0180007000'
##  board is a dict of possible values, e.g. {'A1':'12349', 'A2':'8', ...}
##  r denotes a row, e.g. 'A'
##  c denotes a column, e.g. '3'
##  p denotes a place in the board, e.g. 'D3'
##  v denotes a value,  e.g. '9'


def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]


rows = 'ABCDEFGHI'
cols = '123456789'
grid = cross(rows, cols)
blocks = ([cross(rows, c) for c in cols] + [cross(r, cols) for r in rows] +
          [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')])
adjencency_blocks = dict((s, [u for u in blocks if s in u]) for s in grid)
peers = dict((s, set(sum(adjencency_blocks[s], [])) - set([s])) for s in grid)


################ Unit Tests ################

def test():
    "A set of tests that must pass."
    
    assert len(grid) == 81
    assert len(blocks) == 27
    assert all(len(blocks[s]) == 3 for s in grid)
    assert all(len(peers[s]) == 20 for s in grid)
    assert adjencency_blocks['C2'] == [['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'],
                                       ['C1', 'C2', 'C3', 'C4', 'C5',
                                           'C6', 'C7', 'C8', 'C9'],
                                       ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']]
    assert peers['C2'] == set(['A2', 'B2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2',
                               'C1', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9',
                               'A1', 'A3', 'B1', 'B3'])
    print('All tests pass.')


################ Take an Input Sudoku ################


def possible_board(sudoku):
    """
    Convert sudoku to a dict of possible values, {place: digits}, or
    return False if a contradiction is detected.
    """
    # To start, every place on the board will be filled with any digit; then assign values from the sudoku.
    board = dict((p, '123456789') for p in grid)
    for p, v in read_board(sudoku).items():
        if v in '123456789' and not assign(board, p, v):
            return False  # (Fail if we can't assign v to place p.)
    return board


def read_board(sudoku):
    "Convert sudoku into a dict of {place: char} with '0' for empty places."
    chars = [c for c in sudoku if c in '0123456789']
    assert len(chars) == 81
    return dict(zip(grid, chars))


################ Constraint Propagation ################


def assign(board, p, v):
    """
    Eliminate all the other values (except v) from board[p] and propagate.
    Return resulting board, except return False if a contradiction is detected.
    """
    other_values = board[p].replace(v, '')
    if all(eliminate(board, p, val) for val in other_values):
        return board
    else:
        return False


def eliminate(board, p, v):
    """
    Eliminate v from board[p]; propagate when values or places >= 2.
    Return resulting board, except return False if a contradiction is detected.
    """
    if v not in board[p]:
        return board  # Already eliminated
    board[p] = board[p].replace(v, '')
    # (1) If a place is reduced to one value val, then eliminate val from its peers.
    if len(board[p]) == 0:
        return False  # Contradiction: removed last value
    elif len(board[p]) == 1:
        val = board[p]
        if not all(eliminate(board, p2, val) for p2 in peers[p]):
            return False
    # (2) If a unit p2 is reduced to only one place for a value val, then put it there.
    for p_block in adjencency_blocks[p]:
        v_places = [p2 for p2 in p_block if v in board[p2]]
        if len(v_places) == 0:
            return False  # Contradiction: no place for this value
        elif len(v_places) == 1:
            # d can only be in one place in unit; assign it there
            if not assign(board, v_places[0], v):
                return False
    return board

################ Search ################


def solve_sudoku(sudoku):
    return search(possible_board(sudoku))


def search(board):
    "Using depth-first search and propagation, try all possible values."
    if board is False:
        return False  # Failed earlier
    if all(len(board[p]) == 1 for p in grid):
        return board  # Solved!
    # Chose the unfilled square s with the fewest possibilities
    d = {}
    for p in grid:
        if len(board[p]) > 1: 
            d[p] = len(board[p])
    p = min(d, key=d.get)  
    for v in board[p]:
        if search(assign(board.copy(), p, v)):
            return search(assign(board.copy(), p, v))
    return False
    
################ Display as 2-D grid ################

def display(board):
    "Display the board as a 2-D grid."
    width = 1+max(len(board[p]) for p in grid)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(board[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)


################ Main Function ################

import time

sudoku = '800000000003600000070090200050007000000045700000100030001000068008500010090000400'

assert len(sudoku) == 81

print("The sudoku puzzle is the following:")

display(read_board(sudoku))
start = time.time()
print("\n")
print("-"*85)
print("\n")
print("The possible values to fill the sudoku is the following:")

display(possible_board(sudoku))
print("\n")
print("-"*85)
print("\n")
print("The solution of the sudoku is the following:")

display(solve_sudoku(sudoku))
t = time.time()-start
print('(%.2f seconds)\n' % t)

