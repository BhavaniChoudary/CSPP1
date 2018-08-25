'''

'''
def frequency_graph(dictionary):
    '''
    This fuction takes a dictionary as input and prints the keys and values
    in a format that values are represented in form of no of #'s
    '''
    dict_m = sorted(dictionary.keys())
    for i in dict_m:
        print(i, "-", "#" * dictionary[i])


def main():
    '''
    prints print_dictionary()
    '''
    dictionary = eval(input())
    frequency_graph(dictionary)


if __name__ == '__main__':
    main()
