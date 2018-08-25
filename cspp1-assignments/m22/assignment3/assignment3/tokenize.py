'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    dict_n = {}
    for _ in range(0, len(list_a), 2):
        if list_a[i] not in dict_n:
            dict_n[list_a[i]] = list_a[i+1].split(",")
    return dict_n

def main():
    L = []
    n = int(input())
    for i in range(n):
        list_a_input = input().split(" follows ")
        L.extend(list_a_input)
    print(tokenize(L, n))

if __name__ == '__main__':
    main()
