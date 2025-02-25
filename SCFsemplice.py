import random
# il gioco continua finche il giocatore vuole giocare
risposta = "Y"
pnt_usr = 0
pnt_cpu = 0


while risposta == "Y":
    # cpu sceglie la sua mossa
    cpu = random.randint(1, 3)
    # sfrutto la tipizzazione dinamica di python
    if cpu == 1:
        cpu = "sasso"
    elif cpu == 2:
        cpu = "carta"
    else:
        cpu = "forbice"

    # debug
    print(f"la cpu ha scelto {cpu}")
    # chiedo la mossa all'utente senza validazione
    usr = int(input("""Fai la tua mossa:
    1 -> sasso
    2 -> carta
    3 -> forbice """).strip())
    if usr == 1:
        usr = "sasso"
    elif usr == 2:
        usr = "carta"
    else:
        usr = "forbice"
    # il programma inizia qui
    if cpu == usr:
        print("Pareggio!")
        pnt_usr += 1
        pnt_cpu += 1
    else:
        # quando non c'è pareggio bisogna verificare chi ha vinto
        if cpu == "sasso":
            # l'utente ha scelto carta o forbice
            if usr == "forbice":
                print(f"{cpu} batte {usr}! Hai perso!")
                pnt_cpu += 1
            else:
                print(f"{usr} batte {cpu}! Hai vinto!")
                pnt_usr += 1
        elif cpu == "carta":
            # l'utente ha scelto sasso o forbice
            if usr == "sasso":
                print(f"{cpu} batte {usr}! Hai perso!")
                pnt_cpu += 1
            else:
                print(f"{usr} batte {cpu}! Hai vinto!")
                pnt_usr += 1
        else:
            # l'utente ha scelto carta o sasso
            if usr == "carta":
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