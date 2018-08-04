'''
#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s.Valid vowels
are: 'a', 'e', 'i', 'o', and 'u'
.For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5
@author : BhavaniChoudary
'''
def main():
    '''
    #Assume s is a string of lower case characters.
    #Write a program that counts up the number of vowels contained in the string s.
    Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
    '''
    a_input = input()
    num_vowel = 0
    for char in a_input:
        if char in "aeiou":
            num_vowel += 1
    print(num_vowel)

if __name__ == "__main__":
    main()
