'''
13) Given a string of words, reverse the order of words.
'''

def meth1(string):
    res = string.split()
    return ' '.join(res[::-1])

string = " hello   world  "
print(meth1(string))