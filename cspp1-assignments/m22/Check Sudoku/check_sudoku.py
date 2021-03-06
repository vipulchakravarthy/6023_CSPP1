'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''
def check_column(column_list):
    ''' to check the column
    '''
    temp = []
    flag = 1
    for element in column_list:
        if element not in temp:
            temp.append(element)
        else:
            flag = 0
    return flag

def check_row(row_list):
    ''' to check complete row
    '''
    temp = []
    flag = 1
    for element in row_list:
        if element not in temp:
            temp.append(element)
        else:
            flag = 0
    return flag

def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    for lis in sudoku:
        for element in lis:
            if int(element) > 9 or int(element) < 0:
                return False
    for lis in sudoku:
        row_check = check_row(lis)
        if row_check == 1:
            pass
        else:
            return False
    column_check = []
    for i in range(len(sudoku[0])):
        for lis in sudoku:
            column_check.append(lis[i])
        flag = check_column(column_check)
        if flag == 1:
            pass
        else:
            return False

def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    sudoku = []
    # loop to read 9 lines of input from console
    for _ in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()
