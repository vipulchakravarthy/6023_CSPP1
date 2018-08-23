def mult_matrix(matrix_1, matrix_2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    n = len(matrix_1)
    m = len(matrix_1[0])
    result = [0] * n
    for i in range(n):
        result[i] = [0] * m
    if len(matrix_1[0]) == len(matrix_2):
        for i in range(len(matrix_1)):
            for j in range(len(matrix_2[0])):
                for k in range(len(matrix_2)):
                    result[i][j] += matrix_1[i][k] * matrix_2[k][j]
        return result
    else:
        print("Error: Matrix shapes invalid for multiplication")


def add_matrix(matrix_1, matrix_2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    n = len(matrix_1)
    m = len(matrix_1[0])
    addition = [0] * n
    for i in range(n):
        addition[i] = [0] * m

    if len(matrix_1) == len(matrix_2) and len(matrix_1[0]) == len(matrix_2[0]):
        for i in range(len(matrix_1)):
            for j in range(len(matrix_1[0])):
                addition[i][j] = matrix_1[i][j] + matrix_2[i][j]
        return addition
    else:
        print("Error: Matrix shapes invalid for addition")
        return

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    row_list = []
    matrix_rowsize, matrix_columnsize = map(int, input().split(','))
    matrix = [list(map(int, input().split())) for row in range(matrix_rowsize)]
    return matrix

def main():
    # read matrix 1
    matrix_1 = read_matrix()
    # read matrix 2
    matrix_2 = read_matrix()
    # print(matrix_1)
    # print(matrix_2)
    # add matrix 1 and matrix 2
    sum_matrix = add_matrix(matrix_1, matrix_2)
    print(sum_matrix)
    # multiply matrix 1 and matrix 2
    multi_matrix = mult_matrix(matrix_1, matrix_2)
    print(multi_matrix)

if __name__ == '__main__':
    main()
