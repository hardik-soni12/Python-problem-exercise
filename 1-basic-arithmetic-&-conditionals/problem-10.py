'''
10) Given a basic expression like a op b as input (eg: "3 + 4"), evaluate it safely.
'''

def evaluate_expr_safely(expr):
    expr = expr.replace(' ','') #"16+4"
    
    
    if '+' in expr:
        if expr.count('+') != 1:
            return 'Invalid expression'

        a,b = expr.split('+')
        if not a or not b:
            return f'Invalid expression = {expr}'
        if not a.isdigit() or not b.isdigit():
            return f'Invalid expression = {expr}'
        return int(a) + int(b)
    
    elif '-' in expr:
        if expr.count('-') != 1:
            return 'Invalid expression'

        a,b = expr.split('-')
        if not a or not b:
            return f'Invalid expression = {expr}'
        if not a.isdigit() or not b.isdigit():
            return f'Invalid expression = {expr}'
        return int(a) - int(b)
    
    elif '*' in expr:
        if expr.count('*') != 1:
            return 'Invalid expression'

        a,b = expr.split('*')
        if not a or not b:
            return f'Invalid expression = {expr}'
        if not a.isdigit() or not b.isdigit():
            return f'Invalid expression = {expr}'
        return int(a) * int(b)
    
    elif '/' in expr:
        if expr.count('/') != 1:
            return f'Invalid expression = {expr}'
        
        a,b = expr.split('/')
        if not a or not b :
            return f'Invalid expression = {expr}'
        if not a.isdigit() or not b.isdigit():
            return f'Invalid expression = {expr}'
        if int(b) == 0:
            return f'cannot divide by = {b}'
        return int(a)/int(b)
    
    else:
        return f'Invalid expression = {expr}'
    

expr = "-3 + 4"
print(evaluate_expr_safely(expr))