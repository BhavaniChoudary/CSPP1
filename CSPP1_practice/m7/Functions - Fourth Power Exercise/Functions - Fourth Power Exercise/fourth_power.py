'''
# Exercise: fourth power
# Write a Python function, fourthPower, that takes in one number and returns
 that value raised to the fourth power.
# You should use the square procedure that you defined in an earlier exercise
 exercise (you don't need to redefine square in this box;
# This function takes in one number and returns one number.
'''
def square(x_a):
    '''
    x: int or float.
    '''
    return x_a**2

def fourthpower(x_a):
    '''
    x_a: int or float.
    '''
    # Your code here
    return square(square(x_a))
def main():
    '''
    Fourth_power
    '''
    data = input()
    data = float(data)
    temp = str(data).split('.')
    if temp[1] == '0':
        print(fourthpower(int(float(str(data)))))
    else:
        print(fourthpower(data))

if __name__ == "__main__":
    main()
