'''
# Exercise: GCDRecr
# Write a Python function, gcdRecur(a, b), that takes in two
numbers and returns the GCD(a,b) of given a and b.
# This function takes in two numbers and returns one number.
'''

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    max_n = max(a, b)
    if a == 0 or b == 0:
        return 0
    else:
        for i in range(1, max_n):
            if a % i == 0 and b % i == 0:
                result = i
    return result
    
def main():
    data = input()
    data = data.split()
    print(gcdRecur(int(data[0]),int(data[1])))

if __name__== "__main__":
    main()
