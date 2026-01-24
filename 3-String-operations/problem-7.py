'''
7) Capitalize the first letter of each word in a sentence (without using title()).
'''
def meth1(string):
    l = []
    is_start = True
    for ch in string:
        if ch == ' ':
            l.append(ch)
            is_start = True
        else:
            if is_start:
                l.append(ch.upper())
                is_start = False
            else:
                l.append(ch)

    return ''.join(l)
                 
string = " hello2 world_ python3 "
print(meth1(string))