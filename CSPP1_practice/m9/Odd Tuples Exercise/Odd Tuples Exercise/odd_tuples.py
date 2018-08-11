l#Exercise : Odd Tuples
#Write a python function oddTuples(aTup) that takes a some numbers in the tuple as input and returns a tuple in which contains odd index values in the input tuple  



def oddTuples(aTup):
    '''
    aTup: a tuple
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    btup = ()
    i = 0
    for j in aTup:
    	if i % 2 == 0:
    		btup = btup + tuple(j)
    	i += 1
    return btup

def main():
    data = input()
    data = data.split()
    aTup=()
    for j in range(len(data)):
        aTup += (data[j],)
    print(oddTuples(aTup))
        

if __name__ == "__main__":
    main()
