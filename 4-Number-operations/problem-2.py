'''
2) Check if a year is a leap year (divisible by 4, etc.)
'''
def meth1(year: int):
    if year % 400 == 0:
        return f'{year} is a Leap Year'
    elif year % 100 == 0:
        return f'{year} is not a Leap Year'
    elif year % 4 == 0:
        return f'{year} is a Leap Year'
    else:
        return f'{year} is not a Leap Year'


try:
    year = int(input('Enter the Year to check if its a Leap or not: '))
    if year >= 9999 or year <= 1000:
        print('Year should be of 4 digits')
    else:
        print(meth1(year))
except ValueError:
    print('Input should be Integer')
