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
    l_n = 0.0
    h_n = num
    m_n = (l_n + h_n)/2.0
    while abs(m_n**2-num) >= epsilon:
        if m_n**2 < num:
            l_n = m_n
        else:
            h_n = m_n
        m_n = (l_n + h_n/2.0)
    print(m_n)

    # your code starts here

if __name__ == "__main__":
    main()
