'''
10) Given a number n, print all its divisors.
'''

def divide_by_meth1(n):
    for i in range(1,n+1):
        if (n // i) * i == n:
            print(i, end=' ')

def divide_by_meth2(n):
    for i in range(1,n+1):
        if n % i == 0:
            print(i, end=' ')
        

n = 12
divide_by_meth1(n)
print()
divide_by_meth2(n)
