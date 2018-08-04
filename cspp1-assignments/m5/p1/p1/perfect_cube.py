'''
# Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm

@author : BhavaniChoudary
'''
def main():
    '''
    # input is captured in s
    # watch out for the data type of value stored in s
    # your code starts here
    '''
    cube_num = int(input())
    e_n = 0.01
    i_n = 1
    g_n = 0

    while g_n <= cube_num:
        if abs(g_n**3 -cube_num) < e_n:
            break
        else:
            g_n += i_n
    if abs(g_n**3 - cube_num) >= e_n:
        print(str(cube_num) + " is not a perfect cube")
    else:
        print(str(cube_num) + " is a perfect cube")

if __name__ == "__main__":
    main()
