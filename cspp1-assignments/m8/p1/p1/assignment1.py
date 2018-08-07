'''
# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one number
and returns the factorial of given number.
# This function takes in one number and returns one number.
'''
def factorial(n_m):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    if n_m == 0 or n_m == 1:
        return 1
    else:
        return n_m*factorial(n_m-1)
def main():
    '''
    Factorial
    '''
    a_m = input()
    print(factorial(int(a_m)))  
if __name__ == "__main__":
    main()
