def aggiungiIndice(lista):
    '''Given a list of numbers, create a function which returns the list but with each element's index in the list added to itself'''
    for elem in range(len(lista)):
        lista[elem] = lista[elem] + elem
    print(lista)

lista = [0,0,0,0,0]
print(lista)
aggiungiIndice(lista)
lista = [1,2,3,4,5]
print(lista)
aggiungiIndice(lista)
lista = [5,4,3,2,1]
print(lista)
aggiungiIndice(lista)