'''
# Write a python program to find the square root of the given number
# using approximation method

@author : BhavaniChoudary
'''
def main():
    '''
    # epsilon and step are initialized
    # don't change these values
    '''
    x_i = int(input())
    epsilon = 0.01
    step = 0.1
    g_n = 0.0
    while abs(g_n**2-x_i) >= epsilon:
        if g_n <= x_i:
            g_n += step
        else:
            break
    if abs(g_n**2 - x_i) >= epsilon:
        print('failed')
    else:
        print(str(g_n))

if __name__ == "__main__":
    main()
