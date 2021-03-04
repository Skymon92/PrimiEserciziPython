def sommaNumeriLista(lista):
    '''Lists can be mixed with various types. Your task for this challenge is to sum all the number elements in the given list.
       Create a function that takes a list and returns the sum of all numbers in the list'''
    somma = 0
    for elem in lista:
        if isinstance(elem,int) and isinstance(elem,bool)==False:
            somma += elem
    print(somma)

lista = [1,2,"13","4","645"]
sommaNumeriLista(lista)
lista = [True,False,"123"]
sommaNumeriLista(lista)
lista = [1,2,3,4,5,True]
sommaNumeriLista(lista)