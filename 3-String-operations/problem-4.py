'''
4) Reverse a string without using slicing ([::-1]).
'''

# most optimized and efficient method of reversing a string, if slicing is not alowed.
def meth1(string):
    l = list(string)
    l.reverse()
    return ''.join(l)


string = 'python'
print(meth1(string))