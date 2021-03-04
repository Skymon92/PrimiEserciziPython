#Ogni articolo appartenente alla biblioteca ha una collocazione, un titolo,un autore e un tipo
#(che nel nostro caso semplice sono "libro" o "CD", sottoforma di stringa).
# Ogni articolo deve avere un metodo durataPrestito() che restituisce sotto forma di intero la
# durata del prestito. Ogni prestito in generale dura 30 giorni, cioè questo è il default.
class Articolo:
    def __init__(self,collocazione,titolo,autore,tipo):
        self.collocazione = collocazione
        self.titolo = titolo
        self.autore = autore
        self.tipo = tipo
        self.dPrestito = 30
    def durataPrestito(self):
        return self.dPrestito

# Libro e CD hanno in più un attributo genere ("Filosofia", "Narrativa", "Rock", "Classica"...) e in
# particolare l'implementazione specifica di durataPrestito() nel caso del CD dovrà restituire 7
# giorni invece che 30. 
class Libro(Articolo):
    def __init__(self,genere):
        self.genere = genere

class CD(Articolo):
    def __init__(self,genere):
        super().__init__(collocazione,titolo,autore,tipo)
        self.genere = genere
        self.dPrestito = 7

#Il cliente viene rappresentato dalla classe Cliente, identificato da nome e cognome.
#Ogni oggetto di tipo Cliente avrà due metodi bonusGiorniPrestito() e isStudente().
#Un particolare cliente e` rappresentato dalla classe Studente, che in più ha un attributo
# facolta di tipo stringa che viene inizializzato nel costruttore assieme a nome e cognome e
# contiene il nome della facoltà, p.es. "ingegneria" o "medicina".
# Un Cliente base non ha diritto a bonus di giorni in più per i prestiti (isStudente() restituirà
# sempre False), mentre lo Studente ha un bonus di 10 giorni (isStudente() deve restituire True). 
class Cliente:
    def __init__(self,nome,cognome):
        self.nome = nome
        self.cognome = cognome
        self.bGiorniPrestito = 0
    def bonusGiorniPrestito():
        return self.bGiorniPrestito
    def isStudente():
        return False
class Studente(Cliente):
    def __init__(self,nome,cognome,facolta):
        super().__init__(nome,cognome)
        self.facolta = facolta
    def isStudente():
        return True
    def bonusGiorniPrestito():
        self.dPrestito = self.dPrestito + 10

# Ciascun singolo prestito viene gestito dalla classe Prestito, che ha i seguenti attributi: cliente
# (classe Cliente), articolo (classe Articolo) e dataInizioPrestito (stringa)
# La classe Prestito ha un metodo durataPrestito() che restituisce un intero pari al numero di
# giorni per cui è concesso un prestito di un Articolo. Il calcolo svolto da durataPrestito() deve
# tenere conto della durataPrestito() dell'articolo associato più un eventuale
# bonusGiorniPrestito() che sarà diverso da 0 nel caso di uno studente. 
class Prestito:
    def __init__(self,Cliente,Articolo,dataInizioPrestito):
        self.dataInizioPrestito = dataInizioPrestito
        self.Cliente = Cliente
        self.Articolo = Articolo
    def durataPrestito():
        self.dPrestito = self.dPrestito + self.bGiorniPrestito
        return self.dPrestito

# La classe biblioteca, con attributi denominazione e luogo da inizializzare nel costruttore,
# dovrà offrire questi metodi:
# -getListaPrestiti(), che ritorna una lista di oggetti Prestito
# -getListaArticoli(), che ritorna la lista degli articoli in biblioteca
# -getListaClienti(), che ritorna la lista dei clienti iscritti
# -aggiungiCliente(nome:stringa, cognome:stringa)
# -aggiungiStudente(nome:string, cognome:string, facolta:string)
# -aggiungiArticolo(collocazione:stringa, titolo:stringa, autore:stringa, genere:stringa, tipo:stringa)
# Il tipo è semplicemente 'libro' o 'CD', a seconda dell'articolo che si vuole aggiungere. Nel
# caso il tipo indicato non esista deve comparire un messaggio di errore “Tipo non supportato”.
# -cercaCliente(nome:string, cognome:string) restituisce un oggetto di tipo Cliente
class Biblioteca:
    def __init__(self,denominazione,luogo):
        self.denominazione = denominazione
        self.luogo = luogo
        self.listaClienti=[]
        self.listaArticoli=[]
        self.listaPrestiti=[]
    def getListaPrestiti(self):
        return self.listaPrestiti
    def getListaArticoli(self):
        return self.listaArticoli
    def getListaClienti():
        return self.listaClienti
    def aggiungiCliente(self,nome,cognome):
        clienteDaAggiungere = Cliente(nome,cognome)
        listaClienti.append(clienteDaAggiungere)
    def aggiungiStudente(self,nome,cognome,facolta):
        studenteDaAggiungere = Studente(nome,cognome,facolta)
        listaClienti.append(studenteDaAggiungere)
    def aggiungiArticolo(self,collocazione,titolo,autore,genere,tipo):
        articoloDaAggiungere = Articolo(collocazione,titolo,autore,genere,tipo)
        if articoloDaAggiungere.tipo != "Libro" and Articolo.tipo != "CD":
            print("Tipo non supportato")
        else:
            listaArticoli.append(articoloDaAggiungere)
     def cercaCliente(self,nome,cognome):
         for i in range(len(listaClienti)):
             if nome == listaClienti[i].nome and cognome == listaClienti[i].cognome:
                 return listaClienti[i]