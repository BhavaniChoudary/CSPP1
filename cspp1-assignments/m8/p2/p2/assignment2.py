'''
# Exercise: Assignment-2
# Write a Python function, sumofdigits, that takes in one number
and returns the sum of digits of given number.
# This function takes in one number and returns one number.
'''

def sumofdigits(n_a):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    if n_a == 0:
        return n_a
    return n_a % 10 + sumofdigits(n_a//10)
def main():
    '''
    Sum of individual digits of a given number
    '''
    a_a = input()
    print(sumofdigits(int(a_a)))

if __name__ == "__main__":
    main()
