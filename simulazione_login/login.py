registrati = {"nick99": "Messi",
              "lupo22": "ronnie"}

class Utente:
    def __init__(self):
        self.user = None
        self.password = None

    def check(self):
        print("Benvenuto!")
        print("Effettua il login!")
        while True:
            nome_utente = input("Inserisci il tuo nome utente ").strip()
            password_utente = input("Inserisci la password ").strip()

            try:
                stored_password = registrati[nome_utente]

                if stored_password == password_utente:
                    print("Login effettuato con successo!")
                    break
                elif stored_password != password_utente:
                    print("Password errata!")
                    scelta_utente = input("Vuoi riprovare? (si/no)  ").strip().lower()
                    if scelta_utente == "si":
                        continue
                    else:
                        break

            except KeyError:
                print(f"Errore: il nome utente '{nome_utente}' non è registrato.")
                retry = input("Vuoi riprovare? (si/no) ").strip().lower()
                if retry != "si":
                    print("Uscita dal programma..")
                    break



if __name__ == '__main__':
    utente = Utente()
    utente.check()












"""
#simulazione del signup
def sign_up():
    # Richiesta dell'username
    username = input("Inserisci il tuo username: ")

    # Richiesta della password (la password sarà visibile)
    password = input("Inserisci la tua password: ")

    # Apre il file in modalità append per aggiungere i dati
    with open("utenti.txt", "a") as file:
        file.write(f"{username}:{password}\n")

    print(f"Registrazione completata per {username}")

sign_up()

"""