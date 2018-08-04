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
    num_special  = 0
    for char in a=str_input:
        if char in ("!@#$%^&*"):
        	num_special += 1
        print (" ")

if __name__ == "__main__":
    main()
