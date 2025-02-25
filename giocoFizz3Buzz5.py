# Gioco che sostituisce Fizz a tutti i multipli di 3 e Buzz a tutti i multipli di 5, quando un numero è un multiplo di 3 e 5 scrivo Fizz & Buzz
massimo = int(input("Che numero scegli? ").strip())

# def printFizz():
#    print("FIZZ!")

# def printBuzz():
#    print("BUZZ!")

# def printFizzBuzz():
#    print("FIZZ & BUZZ!")

# def printN(numero):
#    print(numero)

def stampa(parametro):
    print(parametro)


for n in range(1, massimo + 1):
    #DEBUG
    #print(n)
    # Esegui su tutti i numeri multipli di 3 e 5
    # if n % 3 == 0 and n % 5 == 0:
    if n % 15 == 0:
        # print("FIZZ & BUZZ!") è utilizzabile se non uso le funzioni
        # La riga di codice sottostante è una funzione che mi sostituisce la riga di codice sopra
        # printFizzBuzz()
        # Con la funzione stampa posso utilizzare un unica funzione invece di più funzioni
        stampa("FIZZ & BUZZ!")
    elif n % 3 == 0:
        # print("FIZZ!")
        # printFizz()
        stampa("FIZZ!")
    elif n % 5 == 0:
        # print("BUZZ!")
        # printBuzz()
        stampa("BUZZ!")
    else:
        # print(n)
        #printN(n)
        stampa(n)

