'''
1) Print characters present at even index numbers in a string.
'''

def meth1(s):
    return s[::2]

def meth2(s):
    res = ''
    for i in range(0,len(s),2):
        res += s[i]
    return res

def meth3(s):
    res = ''
    for i in range(0,len(s)):
        if i % 2 == 0:
            res += s[i]
    return res

s = 'Python'
print(meth1(s))
print(meth2(s))
print(meth3(s))
