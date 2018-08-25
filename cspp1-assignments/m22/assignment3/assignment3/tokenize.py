'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    '''
    Tokenize
    '''
    dict_n = {}
    for _ in range(0, len(list_a)):
        if list_a[i] not in dict_n:
            dict_n[list_a[i]] = list_a[i+1].split(",")
    return dict_n

def main():
    '''
    Main function
    '''
    l_n = []
    n_n = int(input())
    for _ in range(n_n):
        list_a_input = input().split(" ")
        l_n.extend(list_a_input)
    print(tokenize(l_n, n_n))

if __name__ == '__main__':
    main()
