import random
# il gioco continua finche il giocatore vuole giocare
risposta = "Y"
pnt_usr = 0
pnt_cpu = 0


while risposta == "Y":
    # cpu sceglie la sua mossa
    cpu = random.randint(1, 3)

    # debug
    print(f"la cpu ha scelto {cpu}")
    # chiedo la mossa all'utente senza validazione
    usr = int(input("""Fai la tua mossa:
        1 -> sasso
        2 -> carta
        3 -> forbice """).strip())
    print(f"L'utente ha scelto {usr}")

    # voglio fare in modo che quando cpu > usr vince la cpu e viceversa
    if cpu == usr:
        print("Pareggio!")
        pnt_usr += 1
        pnt_cpu += 1
    else:
        # se la cpu sceglie carta l'algoritmo funziona
        # se la cpu sceglie sasso e l'utente forbice
        if cpu == 1 and usr == 3:
            usr = 0
        # se la cpu sceglie forbici e l'utente sceglie sasso
        elif cpu == 3 and usr == 1:
            usr = 4
        else:
            print("Nessuna conversione da fare")

        if cpu > usr:
            print(f"{cpu} batte {usr}! Hai perso!")
            pnt_cpu += 1
        else:
            print(f"{usr} batte {cpu}! Hai vinto!")
            pnt_usr += 1

    risposta = input("Premi Y per giocare ancora ").strip().upper()


else:
    print("Hai scelto di smettere di giocare")
    print(f"punt cpu = {pnt_cpu}")
    print(f"punt usr = {pnt_usr}")
    if pnt_cpu > pnt_usr:
        print("Hai Persooo")
    elif pnt_cpu == pnt_usr:
        print("Pareggio, rigiochiamo?")
    else:
        print("Mi hai battuto!!!")
