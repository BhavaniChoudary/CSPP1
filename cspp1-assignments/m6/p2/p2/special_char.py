'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
@author = BhavaniChoudary
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    str_input = input()
    n_special = 0
    for char in str_input:
        if char in "!@#$%^&*":
            n_special += 1
        print("")

if __name__ == "__main__":
    main()
