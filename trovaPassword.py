# esempio validazione input: l'utente inserisce la password sbagliata al massimo 3 volte
password = ""
tentativi = 0



while password != "LeoMessi" and tentativi < 3:
    # qui parte il tentatito da inserire la pw corretta
    # passo 1 - incrementare i tentativi
    tentativi += 1

    mex_try = f"Ti sono rimasti {4 - tentativi} tentativi"
    mex_last = "Ultimo tentativo rimasto!"

    mex = mex_try if tentativi < 3 else mex_last
    print(mex)
    password = input("Inserisci la password: ").strip()

if password == "LeoMessi":
    print("Accesso consentito!")
else:
    print("Accesso negato")
