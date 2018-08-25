'''
print dictionary
'''
def print_dictionary(dictionary):
    '''
    This fucntion takes a dictionary as input and prints the keys and values
    in a format and in sorted order
    '''
    k_a = sorted(dictionary.keys())
    for i in k_a:
        print(i, "-", dictionary[i])


def main():
    '''
    calls print_dictionary()
    '''
    dictionary = eval(input())
    print_dictionary(dictionary)


if __name__ == '__main__':
    main()
