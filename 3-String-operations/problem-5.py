'''
5) Count occurrences of a substring in a string.
'''

def meth1(string, substring):
    if not substring:
        return 0
    
    count = 0
    n = len(string)
    m = len(substring)

    for start in range(n - m + 1):
        match = True
        for j in range(m):
            if string[start + j] != substring[j]:
                match = False
                break

        if match:
            count += 1

    return count
    

string = "banana"
substring = 'ana'
print(meth1(string, substring))