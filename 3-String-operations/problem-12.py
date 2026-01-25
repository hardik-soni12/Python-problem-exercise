'''
12) Remove all duplicate characters from a string while preserving order.
'''

def meth1(string):
    check = set()
    res = []
    for ch in string:
        if ch not in check:
            check.add(ch)
            res.append(ch)
        
    return ''.join(res)

string = "AaBbA"
print(meth1(string))