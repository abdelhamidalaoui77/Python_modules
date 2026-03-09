# from datetime import date
# import random
#
# class SoldeInsuffisantException(Exception):
#     pass
#
# class Compte:
#     def __init__(self, solde=0.0):
#
#         self.numero = random.randint(10000, 99999)
#         self.date_ouverture = date.today()
#         self.solde = solde
#
#     def getnumero(self):
#         return self.numero
#
#     def getdate(self):
#         return self.date_ouverture
#
#     def getsolde(self):
#         return self.solde
#
#     def setsolde(self,value):
#        if value >= 0:
#           self.solde = value
#        else:
#            print("veuillez entrer un solde positive!!!")
#
#     def crediter(self,montant):
#         if montant > 0:
#            self.solde += montant
#         else:
#             print("are you joking?????????")
#
#     def debiter(self, montant):
#         if montant < self.solde:
#            self.solde -= montant
#         else:
#             raise SoldeInsuffisantException("Solde insuffisant pour effectuer le retrait.")
#
# from abc import ABC, abstractmethod
#
# class Client(ABC):
#     def __init__(self,Nclient, Dadhésion,compte):
#         self.Nclient = Nclient
#         self.Dadhésion = Dadhésion
#         self.compte = compte
#
#     def getNclient(self):
#         return self.Nclient
#
#     def setNclient(self,value):
#          self.Nclient = value
#
#     def getDadhésion(self):
#         return self.Dadhésion
#
#     def setDadhésion(self,value):
#         self.Dadhésion = value
#
#     def getcompte(self):
#         return self.compte
#
#     def setcompte(self,value):
#         self.compte = value
#
#
#     def equals(self,other):
#         pass
#
# class ClientPhysique(Client):
#     def __init__(self,Nclient, Dadhésion,compte ,nom, date_naissance):
#         Client.__init__(Nclient, Dadhésion,compte)
#         self.nom = nom
#         self.date_naissance = date_naissance
#
#     def equals(self, other):
#         return self.Nclient == other.Nclient


#_______________________________________________
# from datetime import date
# import random
#
# class SoldeInsuffisantException(Exception):
#     pass
#
# class Compte:
#     def __init__(self, solde=0.0):
#         self.numero = random.randint(10000, 99999)
#         self.date_ouverture = date.today()
#         self.solde = solde
#
#     def get_numero(self):
#         return self.numero
#
#     def get_date(self):
#         return self.date_ouverture
#
#     def get_solde(self):
#         return self.solde
#
#     def set_solde(self, value):
#         if value >= 0:
#             self.solde = value
#         else:
#             print("Veuillez entrer un solde positif!!!")
#
#     def crediter(self, montant):
#         if montant > 0:
#             self.solde += montant
#         else:
#             print("Montant invalide!!!")
#
#     def debiter(self, montant):
#         if montant <= self.solde:
#             self.solde -= montant
#         else:
#             raise SoldeInsuffisantException("Solde insuffisant pour effectuer le retrait.")
#
# from abc import ABC, abstractmethod
#
# class Client(ABC):
#     def __init__(self, Nclient, Dadhésion, compte):
#         self.Nclient = Nclient
#         self.Dadhésion = Dadhésion
#         self.compte = compte
#
#     def get_Nclient(self):
#         return self.Nclient
#
#     def set_Nclient(self, value):
#         self.Nclient = value
#
#     def get_Dadhésion(self):
#         return self.Dadhésion
#
#     def set_Dadhésion(self, value):
#         self.Dadhésion = value
#
#     def get_compte(self):
#         return self.compte
#
#     def set_compte(self, value):
#         self.compte = value
#
#     @abstractmethod
#     def equals(self, other):
#         pass
#
# class ClientPhysique(Client):
#     def __init__(self, Nclient, Dadhésion, compte, nom, date_naissance):
#         super().__init__(Nclient, Dadhésion, compte)
#         self.nom = nom
#         self.date_naissance = date_naissance
#
#     def equals(self, other):
#         return self.Nclient == other.Nclient




from datetime import date
import random

class SoldeInsuffisantException(Exception):
    pass

class Compte:
    def __init__(self, solde=0.0):
        self.numero = random.randint(10000, 99999)
        self.date_ouverture = date.today()
        self.solde = solde

    def get_numero(self):
        return self.numero

    def get_date(self):
        return self.date_ouverture

    def get_solde(self):
        return self.solde

    def set_solde(self, value):
        if value >= 0:
            self.solde = value
        else:
            print("Veuillez entrer un solde positif!!!")

    def crediter(self, montant):
        if montant > 0:
            self.solde += montant
        else:
            print("Montant invalide!!!")

    def debiter(self, montant):
        if montant <= self.solde:
            self.solde -= montant
        else:
            raise SoldeInsuffisantException("Solde insuffisant pour effectuer le retrait.")

from abc import ABC, abstractmethod

class Client(ABC):
    def __init__(self, Nclient, Dadhésion, compte):
        self.Nclient = Nclient
        self.Dadhésion = Dadhésion
        self.compte = compte

    def get_Nclient(self):
        return self.Nclient

    def set_Nclient(self, value):
        self.Nclient = value

    def get_Dadhésion(self):
        return self.Dadhésion

    def set_Dadhésion(self, value):
        self.Dadhésion = value

    def get_compte(self):
        return self.compte

    def set_compte(self, value):
        self.compte = value

    @abstractmethod
    def equals(self, other):
        pass

class ClientPhysique(Client):
    def __init__(self, Nclient, Dadhésion, compte, nom, date_naissance):
        super().__init__(Nclient, Dadhésion, compte)
        self.nom = nom
        self.date_naissance = date_naissance

    def equals(self, other):
        return self.Nclient == other.Nclient

# Define a list to store all clients
clients_list = []

# Functions for the menu

def ajouter_client():
    Nclient = input("Entrez le numéro du client: ")
    Dadhésion = input("Entrez la date d'adhésion du client: ")
    solde = float(input("Entrez le solde initial du compte: "))
    compte = Compte(solde)
    nom = input("Entrez le nom du client: ")
    date_naissance = input("Entrez la date de naissance du client: ")
    client = ClientPhysique(Nclient, Dadhésion, compte, nom, date_naissance)
    clients_list.append(client)
    print("Client ajouté avec succès.")

def afficher_clients():
    print("Liste des clients:")
    for client in clients_list:
        print(f"Numéro du client: {client.get_Nclient()}")
        print(f"Date d'adhésion: {client.get_Dadhésion()}")
        print(f"Nom: {client.nom}")
        print(f"Date de naissance: {client.date_naissance}")
        print(f"Numéro de compte: {client.get_compte().get_numero()}")
        print(f"Date d'ouverture du compte: {client.get_compte().get_date()}")
        print(f"Solde du compte: {client.get_compte().get_solde()}")
        print()

def chercher_client():
    Nclient = input("Entrez le numéro du client à chercher: ")
    found = False
    for client in clients_list:
        if client.get_Nclient() == Nclient:
            print("Client trouvé:")
            print(f"Numéro du client: {client.get_Nclient()}")
            print(f"Date d'adhésion: {client.get_Dadhésion()}")
            print(f"Nom: {client.nom}")
            print(f"Date de naissance: {client.date_naissance}")
            print(f"Numéro de compte: {client.get_compte().get_numero()}")
            print(f"Date d'ouverture du compte: {client.get_compte().get_date()}")
            print(f"Solde du compte: {client.get_compte().get_solde()}")
            print()
            found = True
            break
    if not found:
        print("Client non trouvé.")

def supprimer_client():
    Nclient = input("Entrez le numéro du client à supprimer: ")
    for client in clients_list:
        if client.get_Nclient() == Nclient:
            clients_list.remove(client)
            print("Client supprimé avec succès.")
            return
    print("Client non trouvé.")

# Main program
while True:
    print("Menu:")
    print("1. Ajouter un client")
    print("2. Afficher tous les clients")
    print("3. Chercher un client")
    print("4. Supprimer un client")
    print("5. Arrêter le programme")
    choix = input("Entrez votre choix: ")

    if choix == "1":
        ajouter_client()
    elif choix == "2":
        afficher_clients()
    elif choix == "3":
        chercher_client()
    elif choix == "4":
        supprimer_client()
    elif choix == "5":
        print("Programme arrêté.")
        break
    else:
        print("Choix invalide. Veuillez entrer un nombre entre 1 et 5.")

