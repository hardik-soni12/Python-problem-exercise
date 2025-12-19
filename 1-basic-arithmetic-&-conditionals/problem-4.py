'''
4) Given Three numbers, print the largest (no build-in max)
'''
def return_the_largest(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

a,b,c = 15,8,18
print(return_the_largest(a,b,c))