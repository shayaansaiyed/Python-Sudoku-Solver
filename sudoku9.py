

def createTestData():
    return [[2, 9, 0, 0, 0, 0, 3, 0, 0],
            [6, 0, 8, 0, 3, 0, 0, 0, 0],
            [1, 0, 0, 8, 9, 5, 0, 2, 0],
            [0, 0, 7, 2, 8, 9, 0, 4, 0],
            [0, 0, 4, 7, 0, 6, 2, 0, 0],
            [0, 5, 0, 4, 1, 3, 9, 0, 0],
            [0, 2, 0, 9, 6, 8, 0, 0, 7],
            [0, 0, 0, 0, 7, 0, 8, 0, 2],
            [0, 0, 6, 0, 0, 0, 0, 9, 2]]

def SudokuSolverRec(grid, row, col):
    if (row == 9):
        return True

    found = False
    nextRow, nextCol = getNextCoord(row, col)

    if (grid[row][col] != 0):
        found = SudokuSolverRec(grid, nextRow, nextCol)
    else:
        for i in range(1,10):
            if(checkValidPlacement(grid, row, col, i)):
                grid[row][col] = i
                found = SudokuSolverRec(grid, nextRow, nextCol)
                if (found == False):
                    grid[row][col] = 0
    return found

def printNumLine(row):
    for i in range(len(row)):
        print(row[i], end=' ')
        if (i == 2 or i == 5):
            print("|", end=' ')
    print()

def printGrid(grid):
    for i, row in enumerate(grid):
        printNumLine(row)
        if (i == 2 or i == 5):
            print("-"*21)

def getNextCoord(row, col):
    newCol = (col + 1) % 9
    newRow = row
    # moved on to next row
    if (newCol == 0):
        newRow = (row + 1)
    return newRow, newCol

def getPrevCoord(row, col):
    newCol = (col - 1) % 9
    newRow = row
    # move to prev row
    if (newCol == 8):
        newRow = (row - 1) % 9
    return newRow, newCol

def getCoordsOfSquare(row, col):
    # based on (row, col), return array of coordinates
    squareCoord = [[], [], [], [], [], [], [], [], []]

    row_lower_limit = int(row / 3) * 3
    row_upper_limit = (int(row / 3) + 1) * 3

    col_lower_limit = int(col / 3) * 3
    col_upper_limit = (int(col / 3) + 1) * 3

    #Populate for row value
    array_index = 0
    for r in range(row_lower_limit, row_upper_limit):
        for i in range(3):
            squareCoord[array_index].append(r)
            array_index += 1

    #Populate for column value
    array_index = 0
    for i in range(3):
        for c in range(col_lower_limit, col_upper_limit):
            squareCoord[array_index].append(c)
            array_index += 1

    return squareCoord

def checkValidPlacement(grid, row, col, currValue):
    # checks if the value at position (row, col) is valid
    # assumes value at row,col is not 0
    # returns bool

    # check values in column
    for r in range(9):
        if (grid[r][col] == currValue):
            return False

    # check values in row
    for c in range(9):
        if (grid[row][c] == currValue):
            return False

    # check values in square
    squareCoords = getCoordsOfSquare(row, col)
    for r, c in squareCoords:
        if grid[r][c] == currValue:
            return False
    return True


def SolveSudoku(grid):
    SudokuSolverRec(grid, 0, 0)
    return grid



