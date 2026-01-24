'''
10) Replace all spaces in a string with - and remove leading/trailing spaces.
'''
def meth1(string):
    return string.strip().replace(' ', '-')
    
string = " python is awesome "
print(meth1(string))