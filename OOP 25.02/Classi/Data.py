#Classe data
class Data:

    def __init__(self,giorno,mese,anno):
        self.giorno = giorno
        self.mese = mese
        self.anno = anno

    def out(self):
        print("d(",self.giorno,",",self.mese,",",self.anno,")")

    def mod(self,newgiorno,newmese,newanno):
        self.newgiorno = newgiorno
        self.newmese = newmese
        self.newanno = newanno

    def val(self):
        self.giorno = self.newgiorno
        self.mese = self.newmese
        self.anno = self.newanno