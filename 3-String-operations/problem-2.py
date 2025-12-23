'''
2) Remove the first n characters from a string and return the result.
'''
def meth1(string, n):
    if n < 0:
        return 'invalid'
    return string[n:]

def meth2(string, n):
    res = ''
    if n < 0:
        return 'invalid'
    for i in range(n, len(string)):
        res += string[i]
    return res

String= "Programming"
n = 5
print(meth1(String, n))
print(meth2(String, n))