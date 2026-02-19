'''
1) Check if a number is prime (basic version).
'''

def meth1(num):
    if num <= 1:
        return False
    
    if num == 2:
        return True

    if num % 2 == 0:
        return False
    
    for i in range(3, int(num ** 0.5)+ 1, 2):
        if num % i == 0:
            return False
    
    return True


num = 11
print(meth1(num))