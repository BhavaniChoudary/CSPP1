'''
# Exercise: PowerIter
# Write a Python function, iterPower(base, exp), that takes in two
numbers and d the base^(exp) of given base and exp.
# This function takes in two numbers and returns one number.
'''

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    d: int or float, base^exp
    '''
    result = 1
    while exp > 0:
        result = result * base
        exp -= 1
    return result
def main():
    '''
    Iterative power
    '''
    data = input()
    data = data.split()
    print(iterPower(float(data[0]), int(data[1])))
if __name__ == "__main__":
    main()
