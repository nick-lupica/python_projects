import random
contatore = 1
pnt_usr = 0
pnt_cpu = 0

print("Benvenuto al gioco di Carta, Forbice, Sasso!")
print("Le regole sono semplici:")
print("- Sasso batte Forbice")
print("- Forbice batte Carta")
print("- Carta batte Sasso")
print("")


while contatore <= 5:
    scelta_computer = random.randint(1, 3)
    # DEBUG
    # print(scelta_computer)
    print(f"Sei al {contatore} Round!")
    print("Scegli tra sasso, carta e forbice.")
    mossa = input("Quale mossa scegli? ").strip().lower()
    if not mossa.isalpha():
        print("Puoi inserire solo una tra le mosse carta, sasso e forbice")
        print("")
        contatore += 0
        continue
    contatore += 1

#carta = 1, sasso = 2, forbice = 3
    if mossa == "carta" and scelta_computer == 2 or mossa == "sasso" and scelta_computer == 3 or mossa == "forbice" and scelta_computer == 1:
        print(f"Grande, hai vinto il round!")
        print("")
        pnt_usr += 1

    elif mossa == "carta" and scelta_computer == 3 or mossa == "sasso" and scelta_computer == 1 or mossa == "forbice" and scelta_computer == 2:
        print("Mi spiace, hai perso il round!")
        print("")
        pnt_cpu += 1

    elif  mossa == "carta" and scelta_computer == 1 or mossa == "sasso" and scelta_computer == 2 or mossa == "forbice" and scelta_computer == 3:
        print(f"Hai pareggiato il round! Entrambi avete scelto {mossa}. Nessun punto assegnato")
        print("")
    else:
        print("Non hai inserito una mossa valida! Riprova.")
        print("")


else:
    print("I round sono finiti. Scopriamo se hai vinto..")
    print(f"punt cpu = {pnt_cpu}")
    print(f"punt usr = {pnt_usr}")
    if pnt_cpu > pnt_usr:
        print("Hai Perso la partita.")
    elif pnt_cpu == pnt_usr:
        print("Pareggio, rigiochiamo?")
    else:
        print("Complimenti! Hai vinto la partita!")

