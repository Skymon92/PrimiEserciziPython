def numeroMancante(lista):
    '''Create a function that takes a list of numbers between 1 and 10 (excluding one number) and returns the missing number'''
    a = 10
    flag2 = 0
    while a > 0 and flag2 == 0:
        flag = 0
        while flag == 0:
            for elem in lista:
                if a != elem:
                    continue
                else:
                    flag = 1
                    a -= 1
                    break
            if flag == 0:
                flag2 = 1
                flag = 1
    print(a)

lista = [1,2,3,4,6,7,8,9,10]
print(lista)
numeroMancante(lista)
lista = [7,2,3,6,5,9,1,4,8]
print(lista)
numeroMancante(lista)
lista = [10,5,1,2,4,6,8,3,9]
print(lista)
numeroMancante(lista)