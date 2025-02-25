# input -> quale operazione vuoi fare?
# input -> primo numero
# input -> secondo numero
# controllo l'operazione scelta, controllo se operazione o meno
# svolgo il calcolo
# stampo il risultato

print("Programma che crea una calcolatrice")

# Richiesta all'utente del tipo di operazione che vuole fare
operazione = input("""Che tipo di operazione vuoi fare?
 + = somma
 - = sottrazione
 x = moltiplicazione
 / = divisione
 """).strip().lower()

# Richiesta di inserimento dei numeri
x = float(input("Inserisci il primo numero: "))
y = float(input("Inserisci il secondo numero: "))

# Controllo dell'operazione scelta e stampa
if operazione == "somma" or operazione == "+":
    risultato = x + y
elif operazione == "sottrazione" or operazione == "-":
    risultato = x - y
elif operazione == "moltiplicazione" or operazione == "x":
    risultato = x * y
elif operazione == "divisione" or operazione == "/":
    if y == 0:
        print("Errore: divisione per zero non consentita.")
    else:
        risultato = x / y
else:
    print("Operazione non valida. Scegli tra somma, sottrazione, moltiplicazione, divisione.")

print(f"Il risultato della tua {operazione} è {risultato}")











