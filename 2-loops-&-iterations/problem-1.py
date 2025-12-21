'''
1) print all numbers divisible by 5 from a list of up to n:
'''

def div_by_5(n):
    for num in n:
        if num % 5 == 0:
            print(num)


n = [10,43,44,45,23,25,88,90,35]
div_by_5(n)