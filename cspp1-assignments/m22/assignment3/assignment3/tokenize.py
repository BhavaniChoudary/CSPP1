'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    '''
    Tokenize
    '''
    dict_n = {}
    for i in enumerate(0, len(string)):
        if string[i] not in dict_n:
            dict_n[string[i]] = string[i+1].split(",")
    return dict_n

def main():
    '''
    Main function
    '''
    l_n = []
    n_n = int(input())
    for _ in range(n_n):
        string_input = input().split(" ")
        l_n.extend(string_input)
    print(tokenize(l_n))

if __name__ == '__main__':
    main()
