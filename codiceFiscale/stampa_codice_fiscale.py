# Inserisci codice catastale

from stringa_di_testo import StringaDiTesto
from data_di_nascita import DataDiNascita
from comune_di_nascita import ComuneDiNascita
from carattere_di_controllo import CarattereDiControllo

def unisci_codice_fiscale(nome, cognome, anno, mese, giorno, sesso, comune):

    stringa_testo = StringaDiTesto(nome, cognome)
    data_nascita = DataDiNascita(anno, mese, giorno)
    comune_nascita = ComuneDiNascita(comune)

    codice_fiscale_parziale = stringa_testo.genera_codice() + data_nascita.stampa_codice(
        sesso) + comune_nascita.codice_catastale()

    # Calcola il carattere di controllo
    carattere_controllo_calcolato = CarattereDiControllo(codice_fiscale_parziale).calcola_carattere_controllo()

    # Restituisci il codice fiscale completo
    return codice_fiscale_parziale + carattere_controllo_calcolato


if __name__ == '__main__':
    nome = input("Digita il tuo nome ").strip()
    cognome = input("Digita il tuo cognome ").strip()
    anno_nascita = int(input("Digita il tuo anno di nascita ").strip())
    mese_nascita = input("Digita il tuo mese di nascita ").strip()
    giorno_nascita = int(input("Digita il giorno della tua nascita ").strip())
    sesso = input("Digita il tuo sesso (M o F) ").strip()
    comune = input("Digita il comune di nascita ").strip()



    # Stampa CF
    print(unisci_codice_fiscale(nome, cognome, anno_nascita, mese_nascita, giorno_nascita, sesso, comune))

