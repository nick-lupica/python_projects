# Programma che crea una calcolatrice con le 4 operazioni di base e con l'aggiunta di qualche validazione del dato

# Messaggio benvenuto
print("""Ciao, sono una calcolatrice. 
Segui tutti i passaggi per riuscire a ottenere il risultato desiderato.""")

operatore = input("""\nScegli un'operazione da svolgere.
1 + somma
2 - sottrazione
3 x * moltiplicazione
4 / : ÷ divisione
""").strip().lower()

# Le mie condizioni
if (operatore == "1"
        or operatore == "+"
        or operatore == "addizione"
        or operatore == "somma"):
    print("Hai scelto la somma")
    a = input("Inserisci il primo addendo ").strip()
    # controllo se il valore inserito è alfabetico
    if a.isalpha():
        print("Devi inserire un numero")
    else:
        print(F"Hai inserito il numero {a}")
        a = float(a)
        b = input("Inserisci il secondo addendo ").strip()
        if b.isalpha():
            print("Devi inserire un numero")
        else:
            print(f"Hai inserito il numero {b}")
            b = float(b)
            # eseguo la somma
            risultato = round((a + b), 2)
            print(f"il tuo risultato della tua addizione è: {risultato}")

elif (operatore == "2"
      or operatore == "-"
      or operatore == "sottrazione"
      or operatore == "differenza"):
    print("Hai scelto la sottrazione")
    a = input("Inserisci il minuendo ").strip()
    # controllo se il valore inserito è alfabetico
    if a.isalpha():
        print("Devi inserire un numero")
    else:
        print(F"Hai inserito il numero {a}")
        a = float(a)
        b = input("Inserisci il sottraendo ").strip()
        if b.isalpha():
            print("Devi inserire un numero")
        else:
            print(f"Hai inserito il numero {b}")
            b = float(b)
            # eseguo la differenza
            risultato = round((a - b), 2)
            print(f"il tuo risultato della tua sottrazione è: {risultato}")

elif (operatore == "3"
      or operatore == "x"
      or operatore =="*"
      or operatore == "moltiplicazione"
      or operatore == "prodotto"):
    print("Hai scelto la moltiplicazione")
    a = input("Inserisci il primo fattore ").strip()
    # controllo se il valore inserito è alfabetico
    if a.isalpha():
        print("Devi inserire un numero")
    else:
        print(F"Hai inserito il numero {a}")
        a = float(a)
        b = input("Inserisci il secondo fattore ").strip()
        if b.isalpha():
            print("Devi inserire un numero")
        else:
            print(f"Hai inserito il numero {b}")
            b = float(b)
            # eseguo la moltiplicazione
            risultato = round((a * b), 2)
            print(f"il tuo risultato della tua moltiplicazione è: {risultato}")

elif (operatore == "4"
      or operatore == "/"
      or operatore == "÷"
      or operatore == "divisione"
      or operatore == "quoziente"):
    print("Hai scelto la divisione")
    a = input("Inserisci il dividendo ").strip()
    # controllo se il valore inserito è alfabetico
    if a.isalpha():
        print("Devi inserire un numero")
    else:
        print(F"Hai inserito il numero {a}")
        a = float(a)
        b = input("Inserisci il divisore ").strip()
        if b.isalpha():
            print("Devi inserire un numero")
        else:
            print(f"Hai inserito il numero {b}")
            b = float(b)
            if b == 0:
                print("Non è possibile dividere un numero per 0")
            else:
            # eseguo la divisione
                risultato = round((a / b), 2)
                print(f"il tuo risultato è della tua divisione è: {risultato}")
else:
    print("Operazione non valida")
