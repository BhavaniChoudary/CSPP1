def frequency_graph(dictionary):
    '''
    This fuction takes a dictionary as input and prints the keys and values
    in a format that values are represented in form of no of #'s
    '''
    my_dict = sorted(dictionary.keys())
    for i in my_dict:
        print(i, "-", "#" * dictionary[i])


def main():
    '''
    This function reads the input and calls the funtion print_dictionary()
    '''
    dictionary = eval(input())
    frequency_graph(dictionary)


if __name__ == '__main__':
    main()
