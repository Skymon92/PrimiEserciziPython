def numeroUtenti(lista):
    '''Write a function that returns the number of users in a chatroom'''
    if len(lista)==0:
        print("no one online")
    elif len(lista)==1:
        print(lista[0],"online")
    elif len(lista)==2:
        print(lista[0],"and",lista[1],"online")
    else:
        print(lista[0],",",lista[1],"and",len(lista)-2,"more online")

lista = []
numeroUtenti(lista)
lista.append("Paperino")
numeroUtenti(lista)
lista.append("Topolino")
numeroUtenti(lista)
lista.append("Pippo")
lista.append("Pluto")
numeroUtenti(lista)