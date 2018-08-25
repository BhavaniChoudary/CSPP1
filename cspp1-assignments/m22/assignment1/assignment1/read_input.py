'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    '''
    reading input
    '''
    string = " "
    n_a = int(input())
    for i in range(n_a):
        i += 1
        string += input()
        string += '\n'
    print(string)

if __name__ == '__main__':
    main()
