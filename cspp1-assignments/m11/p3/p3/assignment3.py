# Assignment-3
'''
At this point, we have written code to generate a random hand and
display that hand to the user. We can also ask the user for a word
(Python's input) and score the word (using your getWordScore). However,
at this point we have not written any code to verify that a word given by
a player obeys the rules of the game. A valid word is in the word list; and
it is composed entirely of letters from the current hand. Implement the
isvalidword function.
Testing: Make sure the test_isvalidword tests pass. In addition, you will
want to test your implementation by calling it multiple times on the same hand
- what should the correct behavior be? Additionally, the empty string ('') is
not a valid word - if you code this function correctly, you shouldn't need an
additional check for this condition.
Fill in the code for isvalidword in ps4a.py and be sure you've passed the
appropriate tests in test_ps4a.py before pasting your function definition here.
'''

def isvalidword(word, hand, wordlist):
    """
    Returns True if word is in the wordlist and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordlist.
    word: string
    hand: dictionary (string -> int)
    wordlist: list of lowercase strings
    """
    count = 0
    len_ = len(word)
    word = list(word)
    for i in word:
        if i in hand:
            count += 1
    if count == len_ and word in wordlist:
        return True
    return False
def main():
    '''
    Returns True if word is in the wordlist and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or wordlist.
    '''
    word = input()
    n_a = int(input())
    adict = {}
    for i in range(n_a):
        del i
        data = input()
        l_a = data.split()
        adict[l_a[0]] = int(l_a[1])
    l2_a = input().split()
    print(isvalidword(word, adict, l2_a))
if __name__ == "__main__":
    main()
