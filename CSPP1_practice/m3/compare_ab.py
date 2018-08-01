'''
@author : BhavaniChoudary
This program evaluates varA and varB
'''
VARA = 4
VARB = 6
if (isinstance(VARA, str)  or isinstance(VARB, str)):
    print("string involved")
elif VARA > VARB:
    print("bigger")
elif VARA == VARB:
    print("equal")
elif VARA < VARB:
    print("smaller")