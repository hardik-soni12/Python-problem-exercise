'''
3) Check if a string is a palindrome (ignore spaces and case).
'''

def meth1(string):
    string = string.replace(" ",'').lower()
    rev = string[::-1]
    if string == rev:
        return True
    return False

# More efficient O(1) space complexity
def meth2(string):
    a = 0
    b = len(string)-1
    while a < b:
        if string[a] == ' ':
            a+= 1
            continue

        elif string[b] == ' ':
            b -= 1
            continue

        elif string[a].lower() != string[b].lower():
            return False
        
        a += 1
        b -= 1
    
    return True
        

test_case = "A man a plan a canal Panama"
print(meth1(test_case))
print(meth2(test_case))