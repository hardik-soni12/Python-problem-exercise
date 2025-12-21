'''
2) Print number from 1 to n, then same numbers in reverse using loops.
'''

def for_rev_loops(n):
    for i in range(1,n+1):
        print(i, end=' ')

    print()
    for i in range(0,n):
        print(n-i, end=' ')

def for_rev_2(n):
    for i in range(1,n+1):
        print(i,end=' ')
    print()
    
    for i in range(n,0,-1):
        print(i,end=' ')

    

n = 5
for_rev_loops(n)
print()
for_rev_2(n)