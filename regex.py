import re

test_string = input(str)

# a...s$ any five letters starting with a and ending with s.

def first_five_chars_test():
    pattern = "a...s$"

    result = re.match(pattern, test_string)

    if result:
        print ("search succesful.")
    else:
        print ("search unsuccessful.")

first_five_chars_test()

# metacharacters $ and ^
# [] specify a set of characters.

def set_chars_test():
    pattern = "[abc]"


    result = re.match(pattern, test_string)

    if result:
        print ("search succesful.")
    else:
        print ("search unsuccessful.")

set_chars_test()

# a range of characters:

def range_chars_test():
    pattern1 = "[a-r]"
    pattern2 = "[A-N]"
    pattern3 = "[1-9]"


    result1 = re.match(pattern1, test_string)
    result2 = re.match(pattern2, test_string)
    result3 = re.match(pattern3, test_string)

    if result1 or result2 or result3:
        print ("search succesful.")
    else:
        print ("search unsuccessful.")

range_chars_test()

# complement of a character:

def complement_chars_test():
    pattern1 = "[^a-r]"
    pattern2 = "[^0-9]"

    result1 = re.match(pattern1, test_string)
    result2 = re.match(pattern2, test_string)

    if result1 or result2:
        print ("search succesful.")
    else:
        print ("search unsuccessful.")

complement_chars_test()

# .. period -  any two chars will be taken care:

def period_chars_test():
    pattern1 = ".."

    result1 = re.match(pattern1, test_string)

    if result1:
        print ("search succesful.")
    else:
        print ("search unsuccessful.")

period_chars_test()

# ^ - caret - starts with certain chars which is mentioned 

def func6():
    pattern1 = "^a"

    result1 = re.match(pattern1, test_string)

    if result1:
        print ("search succesful.")
    else:
        print ("search unsuccessful.")

func6()
