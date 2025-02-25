print("Questo programmino serve a creare una piccola storia partendo da alcuni imput")

# Chiedi input all'utente
name = input("Dimmi un nome ").strip().capitalize()
if not name.isalpha():  # se il nome non contiene solo lettere riporta errore
    print("Errore: il nome può contenere solo lettere.")
place = input("Dimmi il nome di un luogo ").strip().lower()
fruit= input("Dimmi un frutto ").strip().lower()
number = float(input("Dimmi un numero ").strip())
number_2 = float(input("Dimmi un altro numero ").strip())

# Stampa la storia
print("\nEcco la tua storia")
print(f"""
Un giorno {name} si trovava a {place} quando all'improvviso vide un {fruit} parlante. 
Il frutto era triste perché non riusciva a risolvere un quesito matematico. 
Il {fruit} disse: "Caro {name}, puoi aiutarmi? Ho bisogno di sapere quanto fa {number} * {number_2}. 
Solo se trovo la risposta, potrò tornare a casa!".
{name} ci pensò un attimo, sorrise e rispose: "{number * number_2}", ignorante!
Il {fruit}, spiazzato dalla sua risposta si rattristì, ringrziò comunque {name} per il suo aiuto e
torno a {place} senza batter ciglio.
""")