import json
import os



class Verifica:

    @staticmethod
    def leggi_utenti():
        file_path = "elenco_utenti.json"

        if not os.path.exists(file_path):
            # Se il file non esiste, ritorna un dizionario vuoto
            return {}
        with open(file_path, "r") as file:
            return json.load(file)

    @staticmethod
    def scrivi_utente(utenti):
        file_path = "elenco_utenti.json"
        with open(file_path, "w") as file:
            json.dump(utenti, file, indent=4)
        print(f"Dati salvati nel file {file_path}.")

    @staticmethod
    def registrati(nome_utente, password):
        try:
            utenti = Verifica.leggi_utenti()
            print(utenti)
            if nome_utente not in utenti:
                utenti[nome_utente] = password
                Verifica.scrivi_utente(utenti)
                print("Registrazione avvenuta con successo!")
            else:
                print("Utente già presente nel database!")

        except Exception as e:
            print(f"Errore durante la registrazione: {e}!")

    @staticmethod
    def accedi(nome_utente, password):
        try:
            utenti = Verifica.leggi_utenti()
            for utente, codice in utenti.items():
                if utente == nome_utente and codice == password:
                    print("Login effettuato con successo!")
                    return
                elif utente == nome_utente:
                    print("La password non è corretta!")
                    return
            print("Utente non trovato!")
        except Exception as e:
            print(f"Errore durante l'accesso: {e}!")

    @staticmethod
    def modifica_password(nome_utente, password, nuova_password):
        try:
            utenti = Verifica.leggi_utenti()
            for utente, codice in utenti.items():
                if utente == nome_utente:
                    if codice == password:
                        print("Account verificato! Concessa autorizzazione per modificare password.")

                        if nuova_password != password:
                            utenti[nome_utente] = nuova_password
                            Verifica.scrivi_utente(utenti)
                            print("Password modificata con successo!")
                            return
                        else:
                            print("Non puoi modificare la password riutilizzando quella vecchia!")
                            return
                    else:
                        print("Password errata! Non è possibile modificare la password.")
                        return
            print("Nome utente non trovato!")

        except Exception as e:
            print(f"Errore durante la modifica: {e}")


    def inserisci_dati(self):

        username = input("Inserisci il tuo nome utente ").strip()
        password = input("Inserisci la tua password ").strip()
        return username, password


if __name__ == '__main__':
    verifica = Verifica()

    """while True:
        try:
            print()
            menu = int(input("Benvenuto!\nScegli dal menù una delle seguenti opzioni.\n1-> Registrati\n2-> Esegui l'accesso\n3-> Modifica la password\n4-> Esci\nSeleziona la tua scelta (1,2,3,4). 
             ").strip())

            if menu == 1:
                username = input("Inserisci il tuo nome utente ").strip()
                password = input("Inserisci la tua password ").strip()
                Verifica.registrati(username, password)

            elif menu == 2:
                username = input("Inserisci il tuo nome utente ").strip()
                password = input("Inserisci la tua password ").strip()
                Verifica.accedi(username, password)

            elif menu == 3:
                username = input("Inserisci il tuo nome utente ").strip()
                password = input("Inserisci la tua password ").strip()
                new_password = input("Inserisci la nuova password ").strip()
                Verifica.modifica_password(username, password, new_password)

            elif menu == 4:
                print("Uscita in corso..")
                break

            else:
                print("Digita un numero valido all'interno del menù!")

        except Exception as e:
            print(f"Errore di selezione. Digita un numero valido all'interno del menù!")"""

    while True:
        try:
            print()
            menu = int(input("Benvenuto!\nScegli dal menù una delle seguenti opzioni.\n1-> Registrati\n2-> Esegui l'accesso\n3-> Modifica la password\n4-> Esci\nSeleziona la tua scelta (1,2,3,4). ").strip())

            if menu == 1:
                accesso = Verifica()
                utente, psw = accesso.inserisci_dati()
                Verifica.registrati(utente, psw)

            elif menu == 2:
                accesso = Verifica()
                utente, psw = accesso.inserisci_dati()
                Verifica.accedi(utente, psw)

            elif menu == 3:
                accesso = Verifica()
                utente, psw = accesso.inserisci_dati()
                npsw = input("Inserisci la nuova password ").strip()
                Verifica.modifica_password(utente, psw, npsw)

            elif menu == 4:
                print("Uscita in corso..")
                break

        except Exception as e:
            print(f"Errore di selezione. Digita un numero valido all'interno del menù!")