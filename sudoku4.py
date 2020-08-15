

def createTestData():
    return [[0, 4, 0, 0],
            [0, 0, 0, 2],
            [0, 0, 0, 0],
            [0, 0, 2, 3]]

def SudokuSolverRec(grid, row, col):
    printGrid(grid)
    if (row == 4):
        return True

    found = False
    nextRow, nextCol = getNextCoord(row, col)

    if (grid[row][col] != 0):
        found = SudokuSolverRec(grid, nextRow, nextCol)
    else:
        for i in range(1,5):
            if(checkValidPlacement(grid, row, col, i)):
                grid[row][col] = i
                found = SudokuSolverRec(grid, nextRow, nextCol)
                if (found == False):
                    grid[row][col] = 0
    return found


def printGrid(grid):
    for row in grid:
        print(row)
    print()


def getNextCoord(row, col):
    newCol = (col + 1) % 4
    newRow = row
    # moved on to next row
    if (newCol == 0):
        newRow = (row + 1)
    return newRow, newCol

def getPrevCoord(row, col):
    newCol = (col - 1) % 4
    newRow = row
    # move to prev row
    if (newCol == 3):
        newRow = (row - 1) % 4
    return newRow, newCol

def getCoordsOfSquare(row, col):
    # based on (row, col), return array of coordinates
    squareCoord = [[],[],[],[]]

    if (row == 0 or row == 1):
        squareCoord[0].append(0)
        squareCoord[1].append(0)
        squareCoord[2].append(1)
        squareCoord[3].append(1)
    else:
        squareCoord[0].append(2)
        squareCoord[1].append(2)
        squareCoord[2].append(3)
        squareCoord[3].append(3)

    if (col == 0 or col == 1):
        squareCoord[0].append(0)
        squareCoord[1].append(1)
        squareCoord[2].append(0)
        squareCoord[3].append(1)
    else:
        squareCoord[0].append(2)
        squareCoord[1].append(3)
        squareCoord[2].append(2)
        squareCoord[3].append(3)

    return squareCoord

def checkValidPlacement(grid, row, col, currValue):
    # checks if the value at position (row, col) is valid
    # assumes value at row,col is not 0
    # returns bool

    # check values in column
    for r in range(4):
        if (grid[r][col] == currValue):
            return False

    # check values in row
    for c in range(4):
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
