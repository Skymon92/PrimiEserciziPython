def indiceLettereMaiuscole(stringa):
    '''Create a function that takes a single string as argument and returns an ordered list containing the indices of all capital letters in the string'''
    lista = []
    for elem in range(len(stringa)):
        if stringa[elem].isupper():
            lista.append(elem)
    print(lista)

stringa = "eDaBiT"
indiceLettereMaiuscole(stringa)
stringa = "eQuINoX"
indiceLettereMaiuscole(stringa)
stringa = "determine"
indiceLettereMaiuscole(stringa)
stringa = "STRIKE"
indiceLettereMaiuscole(stringa)