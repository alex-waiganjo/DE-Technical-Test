"""
Write a Python function to check whether a string is pangram or not. (Assume
the string passed in does not have any punctuation)
Note: Pangrams are words or sentences containing every letter of the
alphabet at least once. For example: "The quick brown fox jumps over the
lazy dog"
"""


# Solution

import re   # Use regular expressions


def check_pangram(string):

    # Convert string to lowercase
    string.lower()

    # Get unique letters
    unique_letters = set(re.findall(r'[a-z]', string))

    if (len(unique_letters) == 26):
        print(f'Pangram Test Passed✅: "{string}" is a Pangram')
    else:
        print(f'Pangram Test Failed❌: "{string}" is not a Pangram')


string = "The quick brown fox jumps over the lazy dog"
string2 = "quick brown fox jumps over lazy dog"


# Test string and string2 variables

check_pangram(string)
check_pangram(string2)
