'''
tokenize
'''
import re

def tokenize(string):
    '''
    count
    '''
    a_b = []
    a_c = []
    dictionary_new = {}
    for word in string:
        a_d = (re.sub(r'[^\w\s]', '', word))
        a_b.append(a_d)
    for l in a_b:
        a_c.append(l.split())
    for a in a_c:
        for words in a:
            if words not in dictionary_new.keys():
                dictionary_new[words] = 0
            dictionary_new[words] += 1
    return dictionary_new
def main():
    '''
    main function
    '''
    lis_t = []
    n_n = int(input())
    for i in range(n_n):
        del i
        string = input()
        lis_t.append(string)
    print(tokenize(lis_t))
if __name__ == '__main__':
    main()
