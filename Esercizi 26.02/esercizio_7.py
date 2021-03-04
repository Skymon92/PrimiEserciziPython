class Calculator:
    '''Create methods for the Calculator class that can do the following:
        -Add two numbers
        -Subtract two numbers
        -Multiply two numbers
        -Divide two numbers '''
    
    def somma(self,x,y):
        somma = x + y
        print(somma)
    
    def sottrai(self,x,y):
        sottrazione = x - y
        print(sottrazione)
    
    def moltiplica(self,x,y):
        moltiplicazione = x * y
        print(moltiplicazione)

    def dividi(self,x,y):
        divisione = x / y
        print(divisione)

calculator = Calculator()
calculator.somma(10,5)
calculator.dividi(10,5)