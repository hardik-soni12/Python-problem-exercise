'''
7) Check if a number is even or odd without using if num % 2 == 0 directly.
'''

# using bitwise operator fastest way.
def check_odd_even_meth1(num):
    if (num & 1) == 0:
        return f'{num} is even'
    else:
        return f'{num} is odd'

# using math trick.
def check_odd_even_meth2(num):
    temp = (num//2) * 2
    if temp == num:
        return f'{num} is even'
    else:
        return f'{num} is odd'

num = 61226
print(check_odd_even_meth1(num))
print(check_odd_even_meth2(num))