"""
Write a Python function that checks whether a word or phrase is palindrome or
not.
Note: A palindrome is word, phrase, or sequence that reads the same
backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run"
"""

def is_palindrome(string):
    string = string.lower().replace(" ",'')
    if string == string[::-1]:
        print(f'Palindrome Test Passed✅: "{string}" is a Palindrome')
    else:
        print(f'Palindrome Test Failed❌: "{string}" is not a Palindrome')


# Test Variables
string = "race car"
string2 = 'radar'
string3 = 'madam'
string4 = 'jojo'
string5 = 'check'

is_palindrome(string)
is_palindrome(string2)
is_palindrome(string3)
is_palindrome(string4)
is_palindrome(string5)