def trovaOccorrenzeLista(lista):
    '''Create a function that returns the indices of all occurrences of an item in the list'''
    listaFinale = []
    for i in range(len(lista[0])):
        if lista[1] == lista[0][i]:
            listaFinale.append(i)
    print(listaFinale)


lista = [["a","b","a","c"],"a"]
trovaOccorrenzeLista(lista)
lista = [["a","b","a","c"],"d"]
trovaOccorrenzeLista(lista)
lista = [[1,5,6,5,2,5],5]
trovaOccorrenzeLista(lista)