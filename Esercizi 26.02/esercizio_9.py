def lunghezzaCifre(n):
    ''' Create a function that takes a number num and returns its length'''
    somma = 0
    for i in str(n):
        somma += 1
    print(somma)

n=10
lunghezzaCifre(n)
n=1000
lunghezzaCifre(n)
n=0
lunghezzaCifre(n)