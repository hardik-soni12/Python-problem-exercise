'''
3) Print the sum of numbers from 1 to n (without using the formula).
'''
# sum without formula (O(n) time complexity) .
def sum_of_numbers(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

# sum with formula (O(1) time complexity)
def sum_with_formula(n):
    res = n * (n + 1) // 2
    return res

n = 6
print('without formula : ',sum_of_numbers(n))
print('with formula : ',sum_with_formula(n))