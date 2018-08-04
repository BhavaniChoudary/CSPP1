'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
@author : BhavaniChoudary
'''

def main():
    '''
    Write a program that prints the number of times the string 'bob' occurs in s.
    For example, if s = 'azcbobobegghakl', then your program should print
    Number of times bob occurs is: 2
    '''
    m_a = input()
    s_a = "bob"
    c_a = 0
    for i_a in range(0, len(m_a) - 2):
        j_a = 0
        k_a = i_a
        v_a = 0
        while(j_a < 3 and m_a[k_a] == s_a[j_a]):
            v_a += 1
            k_a += 1
            j_a += 1
            if v_a == 3:
                c_a += 1
    print(c_a)
    

if __name__ == "__main__":
    main()
