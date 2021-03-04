class Cellulare:
    def __init__(self,unaCarica):
        self.soldiDisponibili = unaCarica
        self.numeroChiamate = 0

    def ricarica (self,unaRicarica):
        self.soldiDisponibili = self.soldiDisponibili + unaRicarica
    
    def chiama(self, minutiDurata):
        self.numeroChiamate += 1
        self.soldiDisponibili = self.soldiDisponibili - 0.2*minutiDurata

    def numero404(self):
        return self.soldiDisponibili
    
    def getNumeroChiamate(self):
        return self.numeroChiamate
    
    def azzeraChiamate(self):
        self.numeroChiamate = 0