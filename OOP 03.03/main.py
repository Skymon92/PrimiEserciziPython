from Cellulare import Cellulare

c = Cellulare(5)
print(c.numero404())
c.ricarica(10)
print(c.numero404())
c.chiama(5)
c.chiama(5)
print(c.getNumeroChiamate())
print(c.numero404())
c.azzeraChiamate()
print(c.getNumeroChiamate())