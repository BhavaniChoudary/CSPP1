def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    pass

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    pass

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    matrix = []
    list_input = input().split(',')
    rows, columns = int(list_input[0]), int(list_input[1])
    for _i in range(rows):
        list_matrix_row = input().split()
        if columns == len(list_matrix_row):
            matrix.append([int(i) for i in list_matrix_row])
        else:
            print("Error: Matrix shapes invalid for addition")
            return None
    return matrix

def main():
    # read matrix 1
    matrix_one = read_matrix()
    # read matrix 2
    matrix_two = read_matrix()
    # add matrix 1 and matrix 2
    
    # multiply matrix 1 and matrix 2
    pass

if __name__ == '__main__':
    main()