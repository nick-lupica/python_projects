import random

domande = {
    "Che colore mi piace?": {"A": "Nero", "B": "Arancione", "C": "Marrone", "D": "Giallo"},
    "Qual è il mio numero preferito?": {"A" : "4", "B" : "10", "C" : "22", "D" : "46"},
    "In che nazione sono nato?" : {"A" : "Messico", "B" : "Spagna", "C" : "Italia", "D" : "Giappone"},
    "Quali animali preferisco?" : {"A" : "Cane", "B" : "Gatto", "C" : "Scimmia", "D" : "Serpenti"}
}

salva_risposte_pc = []
salva_risposte_utente = []
contatore = 0
punteggio = 0
for domanda, opzioni in domande.items():
    print(domanda)
    for lettera, chiave in opzioni.items():
        print(f"{lettera}:{chiave}")
    risposta_utente = (input("Scegli la tua risposta? ").strip().upper())
    salva_risposte_utente.append(risposta_utente)
    risposta_cpu_num = random.randint(0, 3)
# Associa il numero alla lettera corrispondente (0 -> 'A', 1 -> 'B', ecc.)
    risposta_cpu = ['A', 'B', 'C', 'D'][risposta_cpu_num]  # Risposta casuale della CPU
    salva_risposte_pc.append(risposta_cpu)
    if risposta_utente == risposta_cpu:
        print("Hai indovinato!")
        contatore +=1
        punteggio += 1
    else:
        print(f"Risposta sbagliata! La risposta corretta era {risposta_cpu}")
        continue

print(f"Il tuo punteggio è stato di {punteggio}/{len(domande)}.")
print(f"Le tue risposte sono state {salva_risposte_utente}.")
print(f"Le risposte corrette erano {salva_risposte_pc}.")
print(f"Percentuale di vittorie: {punteggio / len(domande) * 100}%")
