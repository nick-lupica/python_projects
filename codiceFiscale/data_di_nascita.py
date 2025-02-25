from datetime import datetime
# La classe DataDiNascita dovrà gestire:
# la separazione della stringa inserita in input in giorno, mese e anno
class DataDiNascita:

    def __init__(self, anno, mese, giorno):
        self.anno = str(anno)
        self.mese = str(mese).strip().lower()
        self.giorno = str(giorno)

# La generazione del numero a 2 cifre che identifica l'anno di nascita
    def gestisci_anno(self):
        return self.anno[-2:]

# La conversione del mese di nascita in lettera dell'alfabeto
    def gestisci_mese(self):
        mesi = {
            "1": 'A', "2": 'B', "3": 'C', "4": 'D', "5": 'E', "6": 'H',
            "7": 'L', "8": 'M', "9": 'P', "10": 'R', "11": 'S', "12": 'T', "01": 'A', "02": 'B', "03": 'C', "04": 'D', "05": 'E', "06": 'H',
            "07": 'L', "08": 'M', "09": 'P', "10": 'R', "11": 'S', "12": 'T',
            'gennaio': 'A', 'febbraio': 'B', 'marzo': 'C', 'aprile': 'D', 'maggio': 'E', 'giugno': 'H',
            'luglio': 'L', 'agosto': 'M', 'settembre': 'P', 'ottobre': 'R', 'novembre': 'S', 'dicembre': 'T'
        }

        if self.mese.isdigit():
            return mesi.get(self.mese, "X")
        else:
            return mesi.get(self.mese, "X")

    # Controllo se la data è valida
    def valida_data(self):
        # Se il mese è numerico, posso usarlo direttamente
        if self.mese.isdigit():
            mese_numerico = self.mese
        else:
            # Se il mese è un nome, lo converto nel numero corrispondente
            mese_numerico = {
                'gennaio': '01', 'febbraio': '02', 'marzo': '03', 'aprile': '04',
                'maggio': '05', 'giugno': '06', 'luglio': '07', 'agosto': '08',
                'settembre': '09', 'ottobre': '10', 'novembre': '11', 'dicembre': '12'
            }.get(self.mese, None)

        if mese_numerico is None:
            return False

        try:
            # Verifico se la data è valida con il formato anno-mese-giorno
            datetime.strptime(f"{self.anno}-{mese_numerico}-{self.giorno}", "%Y-%m-%d")
            return True
        except ValueError:
            return False

    # Il calcolo del giorno di nascita in base al sesso
    def gestisci_giorno_sesso(self, sesso):

        if not self.valida_data():
            return "XX"  # Se la data è sbagliata, restituisce "XX"
        giorno = int(self.giorno)
        return f"{giorno + 40}" if sesso.upper() == "F" else f"{giorno:02d}"

# Stampa la concatenazione di anno, mese e giorno
    def stampa_codice(self, sesso):
        codice = self.gestisci_anno() + self.gestisci_mese() + self.gestisci_giorno_sesso(sesso)

        if codice is None:
            return "XXXXXX"  # Valore di fallback
        return codice


if __name__ == '__main__':
    data1 = DataDiNascita("1999", "2", "31")
    print(data1.stampa_codice("M"))  # 99BXX (data non valida)

    data2 = DataDiNascita("2023", "02", "9")
    print(data2.stampa_codice("m"))  # 23BXX (data non valida)

    data3 = DataDiNascita("2000", "2", "20")
    print(data3.stampa_codice("F"))  # 00B69 (data valida)

    data4 = DataDiNascita("1987", "luglio", "10")
    print(data4.stampa_codice("M"))  # 87L10 (valido)

    data5 = DataDiNascita("2005", "dicembre", "25")
    print(data5.stampa_codice("F"))  # 05T65 (valido)
