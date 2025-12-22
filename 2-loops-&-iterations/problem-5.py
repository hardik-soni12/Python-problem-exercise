'''
5) Create a countdown timer from n to 0 (just using sleep print).
'''
import time

def countdown_timer(n):
    for i in range(n, -1, -1):
        print(i)
        time.sleep(1)

n = 5
countdown_timer(n)