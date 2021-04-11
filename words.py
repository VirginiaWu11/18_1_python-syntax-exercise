def print_upper_words(lst,must_start_with=0):
    for word in lst:
        if word[0] in must_start_with:
            print(word.upper())
        

# this should print "HELLO", "HEY", "YO", and "YES"

# print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
#                    must_start_with={"h", "y"})
