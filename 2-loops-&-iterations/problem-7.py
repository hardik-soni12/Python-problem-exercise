'''
7) Given a list, print only elements at even indexes using a loop.
'''

def even_index_meth1(l):
    for i in range(len(l)):
        if i % 2 == 0:
            print(l[i], end=' ')

def even_index_meth2(l):
    for i in range(0, len(l), 2):
        print(l[i], end=' ')


l = [2,4,66,76,23,98,1,96]
even_index_meth1(l)
print()
even_index_meth2(l)