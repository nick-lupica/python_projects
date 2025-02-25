# Terminata la prima parte dell'esercizio, sarà possibile usare la stringa
# fin qui generata per calcolare il carattere di controllo, la cui logica
# dovrebbe essere inserita in una ulteriore classe CarattereDiControllo

class CarattereDiControllo:
    def __init__(self, codice_fiscale):
        self.codice_fiscale = codice_fiscale.upper()  # Prendiamo il codice fiscale in maiuscolo

    # Valori delle lettere per le posizioni dispari
    def valore_lettera_dispari(self, carattere):
        valori = {
            '0': 1, '9': 21, 'I': 19, 'R': 8,
            '1': 0, 'A': 1, 'J': 21, 'S': 12,
            '2': 5, 'B': 0, 'K': 2, 'T': 14,
            '3': 7, 'C': 5, 'L': 4, 'U': 16,
            '4': 9, 'D': 7, 'M': 18, 'V': 10,
            '5': 13, 'E': 9, 'N': 20, 'W': 22,
            '6': 15, 'F': 13, 'O': 11, 'X': 25,
            '7': 17, 'G': 15, 'P': 3, 'Y': 24,
            '8': 19, 'H': 17, 'Q': 6, 'Z': 23
        }
        return valori.get(carattere, 0)

    # Valori delle lettere per le posizioni pari
    def valore_lettera_pari(self, carattere):
        valori = {
            '0': 0, '9': 9, 'I': 8, 'R': 17,
            '1': 1, 'A': 0, 'J': 9, 'S': 18,
            '2': 2, 'B': 1, 'K': 10, 'T': 19,
            '3': 3, 'C': 2, 'L': 11, 'U': 20,
            '4': 4, 'D': 3, 'M': 12, 'V': 21,
            '5': 5, 'E': 4, 'N': 13, 'W': 22,
            '6': 6, 'F': 5, 'O': 14, 'X': 23,
            '7': 7, 'G': 6, 'P': 15, 'Y': 24,
            '8': 8, 'H': 7, 'Q': 16, 'Z': 25
        }
        return valori.get(carattere, 0)

    # Calcola il valore da sommare in base al carattere e alla posizione
    def calcola_valore(self, carattere, pos):
        if carattere.isalpha() or carattere.isdigit():
            if pos % 2 == 1:  # Posizioni dispari
                return self.valore_lettera_dispari(carattere)
            else:  # Posizioni pari
                return self.valore_lettera_pari(carattere)
        return 0

    # Calcola il carattere di controllo
    def calcola_carattere_controllo(self):
        somma = 0
        # Consideriamo solo i primi 15 caratteri
        for i, carattere in enumerate(self.codice_fiscale[:15]):
            valore = self.calcola_valore(carattere, i + 1) 
            somma += valore

        # Il resto della somma modulo 26
        resto = somma % 26
       
        carattere_controllo = chr(65 + resto) 
        return carattere_controllo

# Test del codice
if __name__ == "__main__":
    codice_fiscale = "LPCNCL99C04F158"  
    calcolo = CarattereDiControllo(codice_fiscale)
    carattere_controllo = calcolo.calcola_carattere_controllo()
    print(f"Il carattere di controllo del codice fiscale è: {carattere_controllo}")

