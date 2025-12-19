'''
5) Given a number, check if it is positive, negative, or zero.
'''

def check_num_state(num):
    if num > 0:
        return f'{num} is positive.'
    elif num < 0:
        return f'{num} is negative.'
    else:
        return f'{num} is ZERO'
    
n = int(input('enter num to check: '))
print(check_num_state(n))