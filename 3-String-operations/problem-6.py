'''
6) Given a sentence, find the longest word.
'''

def meth1(sent):
    if not sent:
        return 'empty string'
    
    l = sent.split()
    count = 0
    at_index = 0
    for index in range(len(l)):
        len_of_word = len(l[index])
        if count < len_of_word:
            count = len_of_word
            at_index = index

    return l[at_index]

example = 'Hello\tworld\nPython'
print(meth1(example))