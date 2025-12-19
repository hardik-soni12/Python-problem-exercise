'''
8) Swap two numbers without using a third variable.
'''

# using simple math
def num_swap_meth1(a,b):
    a = a+b
    b = a-b
    a = a-b
    return f'a = {a} \nb = {b}'

# using xor
def num_swap_meth2(a,b):
    a = a ^ b       # a = 12, b = 17 in binary its a = '01100' and b = '10001', answer of both binary using xor will be '11101'
    b = a ^ b       # a = (29)='11101' , b = '17'='10001', answer using xor b = '01100'=(12), 
    a = a ^ b       # a = (29)='11101', b = (12)='01100', answer after xor a = '10001'=(17)
    return f'a = {a} \nb = {b}' #final swapped answer a = 17 and b = 12

# using pythonic way
def num_swap_meth3(a,b):
    a,b = b,a
    return f'a = {a} \nb = {b}'


a = 12
b = 17
print(num_swap_meth1(a,b))
print()
print(num_swap_meth2(a,b))
print()
print(num_swap_meth3(a,b))