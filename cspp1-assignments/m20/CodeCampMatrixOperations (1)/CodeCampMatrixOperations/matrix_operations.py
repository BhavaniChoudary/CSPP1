'''
matrix operations
'''
def mult_matrix(matrix_one, matrix_two):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if len(matrix_one) != len(matrix_two[0]):
        print("Error: Matrix shapes invalid for mult")
        return
    grid = [[0 for i in enumerate(matrix_one)] for j in enumerate(matrix_two[0])]
    for i in range(len(matrix_one)):
        for j in range(len(matrix_two[0])):
            for k in range(len(matrix_two)):
                grid[i][j]  += int(matrix_one[i][k]) * int(matrix_two[k][j])

    return grid
def add_matrix(matrix_one, matrix_two):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    l_new = []
    if len(matrix_one[0]) == len(matrix_two[0]):
        for i in range(len(matrix_one)):
            a_new = []
            for j in range(len(matrix_two[0])):
                a_new.append(int(matrix_one[i][j])+int(matrix_two[i][j]))
            l_new.append(a_new)
        return l_new
    else:
        print("Error: Matrix shapes invalid for addition")
        return None

def read_matrix():
    '''
    read the matrix dimensions from input
    create a list of lists and read the numbers into it
    in case there are not enough numbers given in the input
    print an error message and return None
    error message should be "Error: Invalid input for the matrix"
    '''
    list_input = []
    list_matrix = input().split(",")
    rows, columns = int(list_matrix[0]), int(list_matrix[1])
    for _ in range(int(list_matrix[0])):
        li_matrix = input().split()
        if columns == len(li_matrix):
            list_input.append([int(i) for i in li_matrix])
        else:
            print("Error: Invalid input for the matrix")
            return None
    return list_input

def main():
	'''
	Main function
	'''
    read_matrix_one = read_matrix()
    if read_matrix_one is None:
        exit()
    read2_matrix_two = read_matrix()
    if read2_matrix_two is None:
        exit()

    print(add_matrix(read_matrix_one, read2_matrix_two))
    print(mult_matrix(read_matrix_one, read2_matrix_two))

if __name__ == '__main__':
    main()
