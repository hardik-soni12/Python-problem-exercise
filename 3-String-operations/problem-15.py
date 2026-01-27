'''
15) Find the index of the first occurrence of a substring (no find()).
'''

def meth1(string, sub):
    if sub == '':
        return 0
    
    s = len(string)
    t = len(sub)
    for i in range(s-t+1):
        match = True
        for j in range(t):
            if string[i+j] != sub[j]:
                match = False
                break
        if match:
            return i
        
    return -1

string = "ababc"
sub = "abc"
print(meth1(string, sub))
