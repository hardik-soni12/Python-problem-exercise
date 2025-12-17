'''
3) Build a Simple calculator that supports +, -, *, / based on user choice.
'''

def calculator():
    while True:
        operation = input('select the operation you want to perform: ').strip()
        if operation == 'exit':
            return 'thanku for trying this CLI calc'
        
        if operation not in ['+', '-', '*', '/', '%']:
            print('Invalid operation. Please choose +, -, *, /, %')
            print()
            continue

        
        try:
            num1 = float(input('Enter num1: '))
            num2 = float(input('Enter num2: '))
        except ValueError:
            print('Invalid number input. Please enter numbers only.')
            print()
            continue

        if operation == '+':
            print(f'{num1} + {num2} = {num1 + num2}')
        elif operation == '-':
            print(f'{num1} - {num2} = {num1 - num2}')
        elif operation == '*':
            print(f'{num1} * {num2} = {num1 * num2}')
        elif operation == '/':
            if num2 == 0:
                print('zerodivisor error')
            else:
                print(f'{num1} / {num2} = {num1 / num2}')
        elif operation == '%':
            print(f'{num1} % {num2} = {num1 % num2}')
        else:
            print(f'please enter correct operation to perform')
        print()
    
print(calculator())