'''
4) Print the multiplication table for a given number up to 10.
'''

def multiplication_table(n):
    for i in range(1,11):
        print(f'{n} x {i} = {n*i}')

n = 5
multiplication_table(n)