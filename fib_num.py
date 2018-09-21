"""Generating Fibonnaci numbers considering that each reproducing-age rabbit pair 
gives birth to 1 pair of new-born rabbits after 1 month""" 
n = input("Enter months to run ")
n = int(n)
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
fib(n)
