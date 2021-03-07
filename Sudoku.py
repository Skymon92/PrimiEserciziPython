import numpy
import random

def stampaSudoku():
    print(sudoku[0][0],sudoku[1][0],sudoku[2][0])
    print(sudoku[0][1],sudoku[1][1],sudoku[2][1])
    print(sudoku[0][2],sudoku[1][2],sudoku[2][2])
    print(" ------ "+" ------ "+" ------ ")
    print(sudoku[3][0],sudoku[4][0],sudoku[5][0])
    print(sudoku[3][1],sudoku[4][1],sudoku[5][1])
    print(sudoku[3][2],sudoku[4][2],sudoku[5][2])
    print(" ------ "+" ------ "+" ------ ")
    print(sudoku[6][0],sudoku[7][0],sudoku[8][0])
    print(sudoku[6][1],sudoku[7][1],sudoku[8][1])
    print(sudoku[6][2],sudoku[7][2],sudoku[8][2])

def controlloInserimentoQuadrato(n,quadrato):
    if n in sudoku[quadrato]:
        return True
    else:
        return False
    
def controlloInserimentoRiga(n,nq,nr):
    if nq == 0:
        if n in sudoku[1][nr] or n in sudoku[2][nr]:
            return True
    if nq == 1:
        if n in sudoku[0][nr] or n in sudoku[2][nr]:
            return True
    if nq == 2:
        if n in sudoku[0][nr] or n in sudoku[1][nr]:
            return True
    if nq == 3:
        if n in sudoku[4][nr] or n in sudoku[5][nr]:
            return True
    if nq == 4:
        if n in sudoku[3][nr] or n in sudoku[5][nr]:
            return True
    if nq == 5:
        if n in sudoku[3][nr] or n in sudoku[4][nr]:
            return True
    if nq == 6:
        if n in sudoku[7][nr] or n in sudoku[8][nr]:
            return True
    if nq == 7:
        if n in sudoku[6][nr] or n in sudoku[8][nr]:
            return True
    if nq == 8:
        if n in sudoku[6][nr] or n in sudoku[7][nr]:
            return True

def controlloInserimentoColonna(n,nq,nc):
    if nq == 0:
        if n in sudoku[3][:][nc] or n in sudoku[6][:][nc]:
            return True
    if nq == 1:
        if n in sudoku[4][:][nc] or n in sudoku[7][:][nc]:
            return True
    if nq == 2:
        if n in sudoku[5][:][nc] or n in sudoku[8][:][nc]:
            return True
    if nq == 3:
        if n in sudoku[0][:][nc] or n in sudoku[6][:][nc]:
            return True
    if nq == 4:
        if n in sudoku[1][:][nc] or n in sudoku[7][:][nc]:
            return True
    if nq == 5:
        if n in sudoku[2][:][nc] or n in sudoku[8][:][nc]:
            return True
    if nq == 6:
        if n in sudoku[0][:][nc] or n in sudoku[3][:][nc]:
            return True
    if nq == 7:
        if n in sudoku[1][:][nc] or n in sudoku[4][:][nc]:
            return True
    if nq == 8:
        if n in sudoku[2][:][nc] or n in sudoku[5][:][nc]:
            return True

def inserisciNumero(numero,nq,nr,nc):
    global sudoku
    sudoku[nq][nr][nc] = numero

def generaSudoku():
    '''Nella prima matrice inserisco, in modo randomico, i numeri da 1 a 9
       Nelle restanti 8 tabelle, shifto la prima matrice in maniera tale da ottenere un sudoku risolto'''
    lista = [1,2,3,4,5,6,7,8,9]
    for i in range(0,3):
        for j in range(0,3):
            numeroRandom = random.randint(1,9)
            while numeroRandom not in lista:
                    numeroRandom = random.randint(1,9)
            sudoku[0][i][j] = numeroRandom
            lista.remove(numeroRandom)
    sudoku[1] = numpy.roll(sudoku[0],-3)
    sudoku[2] = numpy.roll(sudoku[0],3)
    sudoku[3] = numpy.roll(sudoku[0],2)
    sudoku[4] = numpy.roll(sudoku[0],-1)
    sudoku[5] = numpy.roll(sudoku[0],-4)
    sudoku[6] = numpy.roll(sudoku[0],4)
    sudoku[7] = numpy.roll(sudoku[0],1)
    sudoku[8] = numpy.roll(sudoku[0],-2)
    return sudoku

def nascondiSudoku():
    '''Con questa funzione vengono nascosti, in maniera casuale, 81-17=64 numeri (81 = # totale di numeri, 17 = # minimo di numeri necessari per giocare)'''
    elenco = []
    counter = 0
    while counter < 64:
        numeroRandom1 = random.randint(0,8)
        numeroRandom2 = random.randint(0,2)
        numeroRandom3 = random.randint(0,2)
        flag = 0
        for i in elenco:
            if [numeroRandom1,numeroRandom2,numeroRandom3] == i:
                flag = 1
                #break
        if flag == 0:
            elenco.append([numeroRandom1,numeroRandom2,numeroRandom3])
            sudoku[numeroRandom1][numeroRandom2][numeroRandom3] = 0
            counter += 1
    return sudoku






######## MAIN ########

# Stampo la tabella di un sudoku 3x3
sudoku = numpy.array([[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]])
stampaSudoku()

# Genero un sudoku
sudoku = generaSudoku()

# Nascondo 64 numeri delle tabelle e chiedo all'utente se è pronto a giocare
sudokuCompleto = sudoku.copy()
sudoku = nascondiSudoku()
risposta = input("Premi una qualsiasi lettera per iniziare a giocare: ")
if risposta != " ":
    stampaSudoku()

# L'utente inizia a giocare
while numpy.array_equal(sudokuCompleto,sudoku) == False:
    numero = int(input("Quale numero da 1 a 9 vuoi inserire? "))
    quadrato = int(input("In quale quadrato da 1 a 9 lo vuoi inserire? "))
    riga = int(input("In quale riga da 1 a 3 lo vuoi inserire? "))
    colonna = int(input("In quale colonna da 1 a 3 lo vuoi inserire? "))

    flag1 = controlloInserimentoQuadrato(numero,quadrato-1)
    if flag1 == True:
        print("ATTENZIONE: Il numero è già presente nel quadrato!")
    
    flag2 = controlloInserimentoRiga(numero,quadrato-1,riga-1)
    if flag2 == True:
        print("ATTENZIONE: Il numero è già presente nella stessa riga")

    flag3 = controlloInserimentoColonna(numero,quadrato-1,colonna-1)
    if flag3 == True:
        print("ATTENZIONE: Il numero è già presente nella stessa colonna")

    inserisciNumero(numero,quadrato-1,riga-1,colonna-1)
    stampaSudoku()

print ("Hai vinto!")