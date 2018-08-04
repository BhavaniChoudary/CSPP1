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
    num = int(input())
    epsilon = 0.01
    mid = num/2 
    low = 0
    high = num
    while abs(mid**2-num) >= epsilon:
        if mid**2 < num:
            low = mid
        else:
            high = mid
        mid = (low+high)/2
    print(str(mid))

    # your code starts here

if __name__ == "__main__":
    main()
