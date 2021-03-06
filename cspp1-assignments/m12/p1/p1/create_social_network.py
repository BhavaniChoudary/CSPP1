'''
    Assignment-1 Create Social Network
'''

def create_social_network(list_a, n):
    '''
    Social Network
    '''
    no_dict = {}
    for i in range(0, len(list_a), 2):
        if list_a[i] not in no_dict:
            no_dict[list_a[i]] = list_a[i+1].split(",")
    return no_dict

    '''
        The data argument passed to the function is a string
        It represents simple social network data
        In this social network data there are people following other people

        Here is an example social network data string:
        John follows Bryant,Debra,Walter
        Bryant follows Olive,Ollie,Freda,Mercedes
        Mercedes follows Walter,Robin,Bryant
        Olive follows John,Ollie

        The string has multiple lines and each line represents one person
        The first word of each line is the name of the person
        The second word is follows that separates the person from the followers
        After the second word is a list_a of people separated by ,

        create_social_network function should split the string on lines
        then extract the person and the followers by splitting each line
        finally add the person and the followers to a dictionary and
        return the dictionary

        Caution: watch out for trailing spaces while splitting the string.
        It may cause your test cases to fail although your output may be right

        Error handling case:
        Return a empty dictionary if the string format of the data is invalid
        Empty dictionary is not None, it is a dictionary with no keys
    '''
def main():
    '''
        handling testcase input and printing output
    '''
    L = []
    n = int(input())
    for i in range(n):
        list_a_input = input().split(" follows ")
        L.extend(list_a_input)
    print(create_social_network(L, n))
main()
