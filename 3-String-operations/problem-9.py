'''
9) Check if two strings are anagrams of each other.
'''

def meth1(string1, string2):
    if len(string1) != len(string2):
        return False
    
    d1 = {}
    d2 = {}
    for ch in string1:
        if ch.lower() not in d1:
            d1[ch.lower()] = 1
        elif ch.lower() in d1:
            a = d1[ch.lower()]
            d1[ch.lower()] = a+1

    for ch in string2:
        if ch.lower() not in d2:
            d2[ch.lower()] = 1
        elif ch.lower() in d2:
            a = d2[ch.lower()]
            d2[ch.lower()] = a+1
    return d1 == d2

        

string1 = "Evil"
string2 = "vile"
print(meth1(string1, string2))