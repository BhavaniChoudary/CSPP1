'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''

def clean_string(string):
    '''
    to remove special characters
    '''
    str = ""
    str_a = 0
    for char in string:
        if char in "!@#$%^&*()":
            str_a += 1
            print("")
    return string

def main():
    '''
    main function
    '''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
