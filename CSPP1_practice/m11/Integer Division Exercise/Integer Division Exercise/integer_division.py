'''
#Ex_aercise: Integer Division Ex_aercise
#Modify the code for integer_division so that this error does not occur.
'''
def integer_division(x_a, a_a):
    """
    x_a: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x_a divided by a.
    """
    count = 0
    while x_a >= a_a:
        count += 1
        x_a = x_a - a_a
    return count

def main():
    '''
    division
    '''
    data = input()
    data = data.split()
    print(integer_division(int(data[0]), int(data[1])))


if __name__ == "__main__":
    main()
