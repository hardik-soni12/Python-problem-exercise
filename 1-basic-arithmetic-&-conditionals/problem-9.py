'''
9) Given a number, check if its within a range [a,b].
'''

def check_within_range(a,b,num):
    
    if a <= num <= b:
        return f'{num} is within a range.'
    elif a >= num >= b:
        return f'{num} is within a range.'
    return f'{num} is not within a range.'

a = 111
b = 10
num = 10
print(check_within_range(a,b,num))