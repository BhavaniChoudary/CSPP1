def tokenize(string, my_dict):
    """
    This functions takes a string as input and cleans it without special charecters and
    returns a dictionary with freqncy of words
    """
    # global my_dict
    for each_word in string:
        if each_word in my_dict:
            my_dict[each_word] += 1
        elif each_word not in my_dict:
            my_dict[each_word] = 1
    return my_dict


def main():
    """
    main function
    """
    my_dict = {}
    no_of_lines = int(input())
    while no_of_lines:
        read_line = input()
        my_string = re.sub("[^ 0-9A-Za-z]", "", read_line)
        my_ans = tokenize(my_string.split(), my_dict)
        no_of_lines -= 1
    print(my_ans)


if __name__ == '__main__':
    main()
