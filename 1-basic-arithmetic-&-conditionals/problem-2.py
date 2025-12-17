'''
2) print the sum of the current number and previous number for numbers 1 to n.
'''

def sum_of_curr_and_prev(n):
    curr = prev = 0
    for i in range(1, n+1):
        curr = i
        print(f'{curr} + {prev} = {curr + prev}')
        prev = curr

sum_of_curr_and_prev(10)