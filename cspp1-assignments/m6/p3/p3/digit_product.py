'''
Given a  number int_input, find the product of all the digits
example:
    input: 123
    output: 6
    @author : BhavaniChoudary
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    int_input = int(input())
    f_n = 0
    if int_input < 0:
        int_input = abs(int_input)
        f_n = 1
        digi_product = 1
        for i in range(len(str(int_input))):
            del i
            k = int_input%10
            digi_product = digi_product * k
            int_input = int_input // 10
            if f_n == 1:
                print('-' + str(digi_product))
            else:
                print(digi_product)

if __name__ == "__main__":
    main()
