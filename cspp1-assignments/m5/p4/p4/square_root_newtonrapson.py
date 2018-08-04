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
    x_n = int(input())
    epsilon = 0.01
    g_n = x_n/2.0
    while abs(g_n*g_n - x_n) >= epsilon:
        g_n = g_n - (((g_n**2) - x_n)/(2*g_n))
    print(str(g_n))
if __name__ == "__main__":
    main()
