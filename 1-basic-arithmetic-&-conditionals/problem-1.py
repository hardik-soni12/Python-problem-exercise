''' 
1) Take two numbers; if their product > 1000 return product, else return sum.
'''

def prod_or_sum(num1, num2):
    if (num1 * num2) > 1000:
        return f'product of {num1} * {num2} = {num1 * num2}'  
    else:
        return f'sum of {num1} + {num2} = {num1 + num2}'
    
print(prod_or_sum(120,9))