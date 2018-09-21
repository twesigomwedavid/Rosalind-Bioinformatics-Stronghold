'''
In modified version of fibonacci rabbit problem,
each reproduction-age pair produces k-pairs to add to the litter
instead of only 1 pair. The rabbits are still immortal.
Function returns total number of rabbits after n months.
'''
def mod_fib(n, k):
    a, b = 1, 1
    for i in range(0, n):
        print(a, end=' ')
        a, b = b, a*3+b
    print()

#mod_fib(n, k)
