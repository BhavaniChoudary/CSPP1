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
    dic_t = {}
    for word in string:
        a_d = (re.sub(r'[^\w\s]', '', word))
        a_b.append(a_d)
    for l in a_b:
        a_c.append(l.split())
    for a in a_c:
        for words in a:
            if words not in dic_t.keys():
                dic_t[words] = 0
            dic_t[words] += 1
    return dic_t
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
