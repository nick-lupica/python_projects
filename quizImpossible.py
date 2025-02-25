import random

# Dobbiamo fare 5 domande
# Le domande le salviamo in una tupla
domande = ("A quale colore sto pensando?", "A quale città sto pensando?",
           "A quale frutto sto pensando?", "A quale animale sto pensando?",
           "A quale professione sto pensando?")

# le opzioni le salviamo in dizionari
# Ciascuna ha 4 opzioni di risposta
colori = {"A": "Magenta", "B": "Vinaccia", "C": "Bordeaux", "D": "Cremisi"}
citta = {"A": "Milano", "B": "Roma", "C": "Bari", "D": "Catania"}
frutti = {"A": "Mango", "B": "Cocco", "C": "Mela", "D": "Pera"}
animali = {"A": "Elefante", "B": "Volpe", "C": "Leone", "D": "Tigre"}
professioni = {"A": "Idraulico", "B": "Cameriere", "C": "Manager", "D": "Avvocato"}

# liste vuote per salvare le risposte dell'utente e le risposte randomiche del pc
risposte_utente = []
risposte_pc = []
# Contatore per il punteggio che aumenterà di 1 a ogni risposta corretta
punteggio = 0

# Funzione per fare una domanda
def fai_domanda(indice_domanda):
    global punteggio
# Stampa la domanda
    print(domande[indice_domanda])

# Seleziona le risposte per questa domanda
    if indice_domanda == 0:
        risposte = colori
    elif indice_domanda == 1:
        risposte = citta
    elif indice_domanda == 2:
        risposte = frutti
    elif indice_domanda == 3:
        risposte = animali
    elif indice_domanda == 4:
        risposte = professioni

    for opzione in risposte:
        print(f"{opzione}: {risposte[opzione]}")
# Per ogni domanda la macchina seleziona una risposta giusta a caso
    risposta_pc = random.randint(0, 3)
    y = ("A", "B", "C", "D")
    # DEBUG risposta corretta pc
    print("La risposta corretta è:", y[risposta_pc])

# salva la risposta corretta in una lista
    risposte_pc.append(y[risposta_pc])

# L'utente inserisce la sua risposta
# Per ogni domanda viene richiesto all'utente di scegliere una risposta e quella viene salvata in una lista (riga di codice risposte_utente.append(risposta_utente)
    risposta_utente = input("Scegli la tua risposta (A, B, C, D): ").strip().upper()

# Per ogni domanda facciamo il confronto tra le due risposte
    if risposta_utente == y[risposta_pc]:
        print("Bravo! Hai indovinato!")
        risposte_utente.append(risposta_utente)
        punteggio += 1
    else:
        risposte_utente.append(risposta_utente)
        print(f"Sbagliato! La risposta corretta era: {y[risposta_pc]}")
# Funzione per avviare il gioco in cui inseriamo il ciclo fino al numero di domande che abbiamo nella tupla "domande"
def gioca():
    for i in range(len(domande)):
        fai_domanda(i)
    print(f"Le risposte corrette erano {risposte_pc}")
    print(f"Le tue risposte erano {risposte_utente}")

# Alla fine delle domande voglio vedere il punteggio
    print(f"Il tuo punteggio finale è: {punteggio} su {len(domande)}")
    print(f"La percentuale di vittorie è stata del {punteggio / (len(domande)) * 100}%")

# Avvia il quiz
gioca() 