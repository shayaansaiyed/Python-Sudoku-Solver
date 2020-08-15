import sudoku9 as s9 
import time as t

def printTW(s, end='\n'):
    for char in s:
        print(char, end='', flush=True)
        t.sleep(0.2)
    print(end)

def getUserInput():
    print()
    print("Hello! Welcome to my Sudoku Solver")
    t.sleep(1)

    print("Please input each line of your Sudoku puzzle, with 0's for blank squares.")
    t.sleep(1)

    print("For example: ")
    t.sleep(1)

    print("Row 1: ", end='')
    t.sleep(0.7)
    printTW("120504000")

    print("\nBegin inputing:")

    inputArray = []
    for i in range(9):
        print("Row {}: ".format(i+1), end='')
        row = input()
        inputArray.append(row)
    
    return(inputArray)

def convertInputToGrid(input):
    # convert input of strings to 2D Array
    grid = []
    for row in input:
        row_array = []
        for char in row:
            row_array.append(int(char))
        grid.append(row_array)
    
    return(grid)
    

def outputSolution(solved_grid):
    return



def main():
    # get user input and convert into 2D array
    user_input = getUserInput()
    grid = convertInputToGrid(user_input)

    print()
    printTW("SOLVING....")

    # call solvefunction from sudoku9 and print out solved
    solved_grid = s9.SolveSudoku(grid)
    s9.printGrid(solved_grid)

main()






