"""
Write a program that accepts a string as input, capitalizes the first letter of each
word in the string, and then returns the result string.
Examples:
"hi"=> returns "Hi"
"i love programming"=> returns "I Love Programming"
"""


# Solutions

sentence = input("write your favorite programming slogan: ")


# Method 1:  {Using title method}
def capitalize(sentence_or_word):
    return f'Method 1: {sentence_or_word.title()}'

#  Output
print(capitalize(sentence))


# Method 2: {Split the words, loop, add the new sentence while capitalizing}
def capitalize_sentence_or_word(sentence):
    empty_sentence = ''
    for sentence_word in sentence.split():
        empty_sentence += sentence_word.capitalize() + ' '
    print(f'Method 2: {empty_sentence}')

# Output
capitalize_sentence_or_word(sentence)
