import re

test_string = input(str)

# a...s$ any five letters starting with a and ending with s.

def first_five_chars_test():
    pattern = "a...s$"

    result = re.match(pattern, test_string)

    if result:
        print ("first_five_chars_test search succesful.")
    else:
        print ("first_five_chars_test search unsuccessful.")

first_five_chars_test()

# metacharacters $ and ^
# [] specify a set of characters.

def set_chars_test():
    pattern = "[abc]"


    result = re.match(pattern, test_string)

    if result:
        print ("set_chars_test search succesful.")
    else:
        print ("set_chars_test search unsuccessful.")

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
        print ("range_chars_test search succesful.")
    else:
        print ("range_chars_test search unsuccessful.")

range_chars_test()

# complement of a character:

def complement_chars_test():
    pattern1 = "[^a-r]"
    pattern2 = "[^0-9]"

    result1 = re.match(pattern1, test_string)
    result2 = re.match(pattern2, test_string)

    if result1 or result2:
        print ("complement_chars_test search succesful.")
    else:
        print ("complement_chars_test search unsuccessful.")

complement_chars_test()

# .. period -  any two chars will be taken care:

def period_chars_test():
    pattern1 = ".."

    result1 = re.match(pattern1, test_string)

    if result1:
        print ("period_chars_test search succesful.")
    else:
        print ("period_chars_test search unsuccessful.")

period_chars_test()

# ^ - caret - starts with certain chars which is mentioned 

def caret_char_test():
    pattern1 = "^a"

    result1 = re.match(pattern1, test_string)

    if result1:
        print ("caret_char_test search succesful.")
    else:
        print ("caret_char_test search unsuccessful.")

caret_char_test()

# $ - dollar - to check if any string ends with certain chars

def dolar_char_test():
    pattern1 = "...a$"

    result1 = re.match(pattern1, test_string)

    if result1:
        print ("dolar_char_test search succesful.")
    else:
        print ("dolar_char_test search unsuccessful.")

dolar_char_test()

# * - star - to check zero or more occurance of the pattrn left to it.

def star_char_test():
    pattern1 = "mi*an"

    result1 = re.match(pattern1, test_string)

    if result1:
        print ("dolar_char_test search succesful.")
    else:
        print ("dolar_char_test search unsuccessful.")

star_char_test()

# + - plus - to check one or more occurance of the pattern left to it.

def plus_char_test():
    pattern1 = "mi+an"

    result1 = re.match(pattern1, test_string)

    if result1:
        print ("dolar_char_test search succesful.")
    else:
        print ("dolar_char_test search unsuccessful.")

plus_char_test()

# ? - question mark - to check zero or one occurance of the pattern left to it.

def question_mark_char_test():

    pattern1 = "mi?an"

    result1 = re.match(pattern1, test_string)

    if result1:
        print ("question_mark_test search succesful.")
    else:
        print ("question_mark_test search unsuccessful.")

question_mark_char_test()

# {n,m} - braces - to check the char at least n and at most m repeitations of the pattern left to it.

def braces_char_test():

    pattern1 = "a{2,5}"
    pattern2 = "[0-9]{3,7}"

    result1 = re.match(pattern1, test_string)
    result2 = re.match(pattern2, test_string)

    if result1 or result2:
        print ("braces_char_test search succesful.")
    else:
        print ("braces_char_test search unsuccessful.")

braces_char_test()

# | -  alternation - to check if there any specified char present in the string.

def alternation_char_test():

    pattern1 = "a|d"

    result1 = re.match(pattern1, test_string)

    if result1:
        print ("alternation_char_test search succesful.")
    else:
        print ("alternation_char_test search unsuccessful.")

alternation_char_test()

# () -  group - to check if any chars present in the string followed by some string.

def group_char_test():

    pattern1 = "(a|d)cv"

    result1 = re.match(pattern1, test_string)

    if result1:
        print ("group_char_test search succesful.")
    else:
        print ("group_char_test search unsuccessful.")

group_char_test()