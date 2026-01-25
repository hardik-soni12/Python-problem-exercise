'''
11) Count vowels and consonants in a string.
'''

def meth1(string):
    vowels = 0
    consonants = 0
    for ch in string:
        if ch.lower() in {'a', 'e', 'i', 'o', 'u'}:
            vowels += 1
        elif ch.isalpha():
            consonants += 1

    return f'vowels = {vowels}, consonants = {consonants}'


string = 'A1 e!O?'
print(meth1(string))