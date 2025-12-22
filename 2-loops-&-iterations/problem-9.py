'''
9) Count how many numbers in a list are positive, negative, and zero.
'''

numbers = [10, -3, 0, 25, -7, 0, 4, -1, 0, 8]

positive = negative = zero = 0

for num in numbers:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

print(f'positive = {positive}\nnegative = {negative}\nzero = {zero} ')