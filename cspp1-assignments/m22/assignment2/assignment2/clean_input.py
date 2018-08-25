'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''

def clean_string(string):
    str_input = input()
    n_special = 0
    for char in str_input:
        if char in "!@#$%^&*":
        	print("")

def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
