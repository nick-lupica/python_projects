# immettere da tastiera un numero n
# realizzare un programma che elenchi i numeri da 1 a n tale che
    # se il numero è multiplo di 3, stampa fizz
    # se il numero è multiplo di 5, stampa buzz
    # se il numero è multiplo di 3 e di 5, stampa fizzbuzz

print("Giochiamo a fizz3buzz5!!!")
n = int(input("Fino a quale numero vuoi giocare? "))

# def fizz3(a):
    # stringa = "fizz" if (a % 3) == 0 else ""
    # return stringa

fizz3 = lambda a: "fizz" if (a % 3) == 0 else ""

# def buzz5(a):
    # stringa = "buzz" if (a % 5) == 0 else ""
    # return stringa

buzz5 = lambda a: "buzz" if (a % 5) == 0 else ""

for i in range(1, n+1):
   riga = fizz3(i) + buzz5(i)
   if riga == "":
       riga = i
   print(riga)


