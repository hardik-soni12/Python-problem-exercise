'''
6) Keep taking input until user types "exit"; then print how many valid inputs were given.
'''

def valid_input():
    total = 0
    while True:
        user_input = input('Enter valid input : ')
        if user_input == 'exit':
            return total
        total += 1

print(valid_input())