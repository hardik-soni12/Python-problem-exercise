'''
8) Check if a string contains any digits using a loop (no regex, no .isdigit() shortcut).
'''

def meth1(string):
    l = ['0', '1', '2', '3', '4', '5', '6' , '7', '8', '9']
    for ch in string:
        if ch in l:
            return True
    
    return False


string = 'hello_5_world'
print(meth1(string))