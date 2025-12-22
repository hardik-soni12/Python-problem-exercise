'''
8) Compute factorial of n using a loop.
'''

def factorial_of_n(n):
    res = 1
    if n == 0 or n == 1 :
        return 1
    for i in range(1,n+1):
        res *= i
    
    return res

n = 5
print(factorial_of_n(n))