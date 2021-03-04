def invertiStringa(stringa):
    '''Create a function that takes a string(will be a person's first and last name) and returns a string with the first and last name swapped'''
    lista = stringa.split()
    lista.reverse()
    stringa = lista[0] + " " + lista[1]
    print(stringa)

stringa = "Jack Kirby"
invertiStringa(stringa)
stringa = "Danny O'Neil"
invertiStringa(stringa)