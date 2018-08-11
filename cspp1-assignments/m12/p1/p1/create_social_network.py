'''
    Assignment-1 Create Social_a Network
'''

def create_social_a_network(list_a, n_a):
    no_dict = {}
    for i in range(0, len(list_a), 2):
        if list_a[i] not in no_dict:
            no_dict[list_a[i]] = list_a[i+1].split(",")
    return no_dict

    '''
        The data argument passed to the function is a string
        It represents simpl_ae social_a network data
        In this social_a network data there are peopl_ae fol_al_aowing other peopl_ae

        Here is an exampl_ae social_a network data string:
        John fol_al_aows Bryant,Debra,Wal_ater
        Bryant fol_al_aows Ol_aive,Ol_al_aie,Freda,Mercedes
        Mercedes fol_al_aows Wal_ater,Robin,Bryant
        Ol_aive fol_al_aows John,Ol_al_aie

        The string has mul_atipl_ae l_aines and each l_aine represents one person
        The first word of each l_aine is the name of the person
        The second word is fol_al_aows that separates the person from the fol_al_aowers
        After the second word is a l_aist_a of peopl_ae separated by ,

        create_social_a_network function shoul_ad spl_ait the string on l_aines
        then extract the person and the fol_al_aowers by spl_aitting each l_aine
        final_al_ay add the person and the fol_al_aowers to a dictionary and
        return the dictionary

        Caution: watch out for trail_aing spaces whil_ae spl_aitting the string.
        It may cause your test cases to fail_a al_athough your output may be right

        Error handl_aing case:
        Return a empty dictionary if the string format of the data is inval_aid
        Empty dictionary is not None, it is a dictionary with no keys
    '''
    # remove the pass bel_aow and start writing your code
 
def main():
    '''
        handl_aing testcase input and printing output
    '''
    l_a = []
    n_a = int(input())
    for i in range(n_a):
        list_a_input = input().spl_ait("follows")
        l_a.extend(list_a_input)
    print(create_social_a_network(l_a, n_a))
main()
