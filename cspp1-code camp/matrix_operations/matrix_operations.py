'''
the program is to find the addition of matrices and multiplication of matrices
'''
def mult_matrix(matrix_1, matrix_2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    row = len(matrix_1)
    k_length = len(matrix_2)
    column = len(matrix_2[0])
    result = [0] * row
    for iterate in range(row):
        result[iterate] = [0] * column
    if len(matrix_1[0]) == len(matrix_2):
        for i in range(row):
            for j in range(column):
                for k in range(k_length):
                    result[i][j] += matrix_1[i][k] * matrix_2[k][j]
        return result
    if len(matrix_1[0]) != len(matrix_2):
        print("Error: Matrix shapes invalid for mult")

def add_matrix(matrix_1, matrix_2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    row = len(matrix_1)
    column = len(matrix_1[0])
    addition = [0] * row
    for iterate in range(row):
        addition[iterate] = [0] * column
    if len(matrix_1) == len(matrix_2) and len(matrix_1[0]) == len(matrix_2[0]):
        for i in range(row):
            for j in range(column):
                addition[i][j] = matrix_1[i][j] + matrix_2[i][j]
        return addition
    if len(matrix_1) != len(matrix_2) and len(matrix_1[0]) != len(matrix_2[0]):
        print("Error: Matrix shapes invalid for addition")

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    matrix = []
    matrix_rowsize, matrix_columnsize = map(int, input().split(','))
    for _ in range(matrix_rowsize):
        row = list(map(int, input().split()))
        assert len(row) == matrix_columnsize
        matrix.append(row)
    return matrix
def main():
    '''
    the program is to perform the matrix operations
    '''
    # read matrix 1
    try:
        matrix_1 = read_matrix()
    # read matrix 2
        matrix_2 = read_matrix()
    except Exception as e:
        print("Error: Invalid input for the matrix")
    # print(matrix_1)
    # print(matrix_2)
    # add matrix 1 and matrix 2
    else:
        sum_matrix = add_matrix(matrix_1, matrix_2)
        print(sum_matrix)
    # multiply matrix 1 and matrix 2
        multi_matrix = mult_matrix(matrix_1, matrix_2)
        print(multi_matrix)
if __name__ == '__main__':
    main()
