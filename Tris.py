
tabella = [0,0,0,0,0,0,0,0,0]

def mossa(tabella):
    azione = input ("Scegli quale posizione marcare (da 1 a 9):")-1


def stampaTabella():
    segno = ["", "", "", "", "", "", "", "", ""]
    for i in range(0,9):
        if tabella[i] == 1:
            segno[i] = "X"
        elif tabella[i] == 2:
            segno[i] = "O"
        elif tabella[i] == 0:
            segno[i] = " "
    print ("         | " + str(segno[0]) + " | " + str(segno[1]) + " | " + str(segno[2]) + " | ")
    print ("         | " + str(segno[3]) + " | " + str(segno[4]) + " | " + str(segno[5]) + " | ")
    print ("         | " + str(segno[6]) + " | " + str(segno[7]) + " | " + str(segno[8]) + " | ")

def controlloVittoria(partitaInCorso):
    if (tabella[0]==tabella[1] and tabella[1]==tabella[2] and tabella[1]!=0) or (tabella[0]==tabella[3] and tabella[3]==tabella[6] and tabella[3]!=0) or (tabella[6]==tabella[7] and tabella[7]==tabella[8] and tabella[7]!=0) or (tabella[2]==tabella[5] and tabella[5]==tabella[8] and tabella[5]!=0) or (tabella[0]==tabella[4] and tabella[4]==tabella[8] and tabella[4]!=0) or (tabella[2]==tabella[4] and tabella[4]==tabella[6] and tabella[4]!=0):
        partitaInCorso = False
        print("Hai vinto")
    return partitaInCorso
    

def tris (tabella):
    partitaInCorso = True
    while partitaInCorso == True:
        i = int(input("Scegli la posizione (da 1 a 9)"))
        if tabella[i-1] == 0:
            tabella[i-1] = 1
            stampaTabella()
        else:
            tris(tabella)
        partitaInCorso = controlloVittoria(partitaInCorso) #avrei potuto anche utilizzare la variabile globale partitaInCorso nella funzione controlloVittoria
        if 0 not in tabella:
            partitaInCorso = False
            print ("PAREGGIO")
        
        if partitaInCorso == True:
            i = int(input("Scegli la posizione (da 1 a 9)"))
            if tabella[i-1] == 0:
                tabella[i-1] = 2
                stampaTabella()
            else:
                tris(tabella)
            partitaInCorso = controlloVittoria(partitaInCorso)
            if 0 not in tabella:
                partitaInCorso = False
                print("PAREGGIO")

        

tris(tabella)