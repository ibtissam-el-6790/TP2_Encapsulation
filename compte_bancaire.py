class CompteBancaire:
    def __init__(self, titulaire, solde_initial=0):
        self._titulaire = titulaire
        self.__solde = solde_initial
        self._operations = []   # historique

    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
            self._operations.append(f"Dépôt : +{montant}")
        else:
            print("Montant invalide.")

    def retirer(self, montant):
        if 0 < montant <= self.__solde:
            self.__solde -= montant
            self._operations.append(f"Retrait : -{montant}")
        else:
            print("Fonds insuffisants ou montant invalide.")

    @property
    def solde(self):
        return self.__solde

    def afficher_operations(self):
        for op in self._operations:
            print(op)

    def __str__(self):
        return f"Titulaire : {self._titulaire}, Solde : {self.solde} €"

    # Protection totale du solde
    def __setattr__(self, nom, valeur):
        if nom == "solde":  
            raise AttributeError("Solde protégé — utilisez deposer() ou retirer()")
        super().__setattr__(nom, valeur)


class CompteEpargne(CompteBancaire):
    def __init__(self, titulaire, solde_initial=0, taux=0.02):
        super().__init__(titulaire, solde_initial)
        self._taux = taux

    def calculer_interet(self):
        return self.solde * self._taux


if __name__ == "__main__":
    compte = CompteBancaire("Ali", 1000)

    compte.deposer(200)
    compte.retirer(150)

    print(compte)
    print("Solde accessible (lecture) :", compte.solde)

    compte.solde = 500
