def print_dictionary(dictionary):
    '''
    This fucntion takes a dictionary as input and prints the keys and values
    in a format and in sorted order
    '''
    # print(len(dictionary))
    new_keys = sorted(dictionary.keys())
    for i in new_keys:
        print(i, "-", dictionary[i])


def main():
    '''
    This function reads the input and calls the funtion print_dictionary()
    '''
    dictionary = eval(input())
    print_dictionary(dictionary)


if __name__ == '__main__':
    main()