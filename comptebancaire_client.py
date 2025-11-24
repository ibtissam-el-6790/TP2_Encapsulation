from datetime import datetime

class CompteBancaire:
    compteur_id = 1  # Pour générer un identifiant unique

    def __init__(self, solde_initial=0.0):
        self.__solde = solde_initial
        self.id = CompteBancaire.compteur_id
        CompteBancaire.compteur_id += 1
        self.operations = []  # Liste pour stocker les opérations

    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
            self.operations.append((datetime.now(), "Dépôt", montant))
        else:
            print("Montant de dépôt invalide.")

    def retirer(self, montant):
        if 0 < montant <= self.__solde:
            self.__solde -= montant
            self.operations.append((datetime.now(), "Retrait", montant))
        else:
            print("Montant de retrait invalide ou solde insuffisant.")

    def get_solde(self):
        return self.__solde

    def relevé(self):
        print(f"Relevé du compte {self.id} :")
        for op in self.operations:
            date_str = op[0].strftime("%Y-%m-%d %H:%M:%S")
            print(f"{date_str} - {op[1]} : {op[2]}€")
        print(f"Solde actuel : {self.__solde}€\n")



class Client:
    def __init__(self, nom):
        self.nom = nom
        self.comptes = []  # Liste de comptes

    def ajouter_compte(self, compte):
        self.comptes.append(compte)

    def afficher(self):
        print(f"Client : {self.nom}")
        for c in self.comptes:
            print(f"  Compte {c.id} : Solde {c.get_solde()}€")
        print()

# Création d'un client
cli = Client("Yassir")

# Création de deux comptes
compte1 = CompteBancaire(100)
compte2 = CompteBancaire(500)

# Ajout des comptes au client
cli.ajouter_compte(compte1)
cli.ajouter_compte(compte2)

# Effectuer des opérations
compte1.deposer(200)
compte1.retirer(50)

compte2.retirer(100)
compte2.deposer(300)

# Affichage des informations du client
cli.afficher()

# Affichage des relevés détaillés
compte1.relevé()
compte2.relevé()
