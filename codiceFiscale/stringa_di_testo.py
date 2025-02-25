# La classe StringaDiTesto gestisce nome e cognome

class StringaDiTesto:
    vocali = ("A", "E", "I", "O" ,"U")
    consonanti = ("B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "Z", "X", "Y", "W")

    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

# Codice che separa vocali da consonanti e li stampa in cons e voc
    def separa_cons_e_voc(self, stringa):
        cons = ""
        voc = ""
        for lettera in stringa.upper():
            if lettera in self.vocali:
                voc += lettera
            elif lettera in self.consonanti:
                cons += lettera
        return cons, voc

# Metodo che gestice le prime 3 lettere del cognome
    def gestisci_nome(self, stringa):
        cons, voc = self.separa_cons_e_voc(stringa)
        stringa_nome = (cons + voc).replace(" ", "")
        if not stringa_nome:  # Aggiunto controllo
            return "XXX"
        if len(cons) >= 4:
            return stringa_nome[0] + stringa_nome[2] + stringa_nome[3]
        elif len(cons) == 3 or len(stringa_nome) >= 3:
            return stringa_nome[:3]
        elif len(cons) == 2 or len(stringa_nome) >= 2:
            return stringa_nome + "X"
        elif len(cons) == 1 or len(stringa_nome) == 1:
            return stringa_nome + "XX"
        else:
            return "XXX"

    # Metodo che gestice le prime 3 lettere del cognome
    def gestisci_cognome(self, stringa):
        cons, voc = self.separa_cons_e_voc(stringa)
        stringa_cognome = (cons + voc).replace(" ", "").replace("'", "")
        if not stringa_cognome:  # Aggiunto controllo
            return "XXX"
        if len(stringa_cognome) >= 3:
            return stringa_cognome[:3]
        elif len(stringa_cognome) == 2:
            return stringa_cognome + "X"
        elif len(stringa_cognome) == 1:
            return stringa_cognome + "XX"
        else:
            return "XXX"

# Metodo che mi ritorna la concatenazione delle prime 3 lettere del cognome + le prime 3 lettere del nome
    def genera_codice(self):
        cognome_codice = self.gestisci_cognome(self.cognome)
        nome_codice = self.gestisci_nome(self.nome)

        if cognome_codice is None:
            cognome_codice = "XXX"  # Imposta un valore di fallback per il cognome
        if nome_codice is None:
            nome_codice = "XXX"  # Imposta un valore di fallback per il nome

        return cognome_codice + nome_codice


if __name__ == '__main__':

    nome = input("Digita il tuo nome ").strip()
    cognome = input("Digita il tuo cognome ").strip()

    obj = StringaDiTesto(nome, cognome)

    print(obj.genera_codice())
