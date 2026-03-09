# class compte:
#     def __init__(self,num,d_ouv,solde):
#         self.numéro = num
#         self.dt_ouverture = d_ouv
#         self.solde = solde
#
#
#
#
#
#
# from datetime import date
#
# date_aujourdhui = date.today()
#
# print(date_aujourdhui)
#
#
#
#
#
# import random
#
# nombre_aleatoire = random.randint(10000, 99999)
#
# print(nombre_aleatoire)


#______________________________________________________________________________________
from datetime import date
import random

class SoldeInsuffisantException(Exception):
    pass

class Compte:
    def __init__(self, solde=0.0):

        self.numero = random.randint(10000, 99999)
        self.date_ouverture = date.today()
        self.solde = solde



    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, value):
        if not isinstance(value, int):
            raise ValueError("Le numéro du compte doit être un entier.")
        self._numero = value

    @property
    def date_ouverture(self):
        return self._date_ouverture

    @date_ouverture.setter
    def date_ouverture(self, value):
        if not isinstance(value, date):
            raise ValueError("La date d'ouverture doit être un objet date.")
        self._date_ouverture = value

    @property
    def solde(self):
        return self._solde

    @solde.setter
    def solde(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Le solde doit être un nombre.")
        self._solde = value

    def crediter(self, montant):
        self.solde += montant

    def debiter(self, montant):
        if montant > self.solde:
            raise SoldeInsuffisantException("Solde insuffisant pour effectuer le retrait.")
        self.solde -= montant

# Exemple d'utilisation
compte1 = Compte()
print(f"Numéro: {compte1.numero}, Date d'ouverture: {compte1.date_ouverture}, Solde: {compte1.solde}")

compte2 = Compte(solde=1000.0)
print(f"Numéro: {compte2.numero}, Date d'ouverture: {compte2.date_ouverture}, Solde: {compte2.solde}")

compte2.debiter(500.0)
print(f"Nouveau solde après retrait: {compte2.solde}")
# l=[]
# def ajout():
#     nom_emp=input("donner un nom :")
#     salaire=float(input("donner un salaire :"))
#     grade=input("donner une grade :")
#     emp=Employe(nom_emp,salaire,grade)
#     Lemp.append(emp)
# def Recherche(code):
#     for x in Lemp:
#         if x.code_emp == code:
#             return x
#
# def suppression(num):
#     if Recherche(num):
#         Lemp.remove(Recherche(num))
#         print("suppression éffectuée")
#     else:
#         print("Aucun Joueur avec ce code")
# def Affichage():
#     for i in Lemp:
#         print(i)
# def exporter():
#     f=open("employe.txt","w")
#     for x in Lemp:
#         f.writelines(f"{x}\n")
# while(True):
#     print("Menu des commandes:")
#     print("1.Ajouter un Employe")
#     print("2.Chercher un Employe")
#     print("3.Afficher tout les Employes")
#     print("4.Supprimer un Employe")
#     print("5.Quitter")
#     print("Tapper le N° de votre choix :")
#     x=int(input())
#     if x==1:
#         ajout()
#     elif x==2:
#         n=int(input(("Donner le N°emp à chercher :")))
#         if Recherche(n):
#             print(Recherche(n))
#         else:
#             print("Aucun Employe avec ce N°")
#     elif x==3:
#         Affichage()
#     elif x==4:
#         d=int(input("donner le N°emp à Supprimer :"))
#         suppression(d)
#     elif x==5:
#         break
#     else:
#         print("Donner un choix entre 1 et 6")












# from datetime import date
# import random
#
# class SoldeInsuffisantException(Exception):
#     pass
#
# class Compte:
#     def __init__(self, numero=None, solde=0.0):
#         if numero is None:
#             numero = self.generer_numero()
#         self.numero = numero
#         self.date_ouverture = date.today()
#         self.solde = solde
#
#     def __str__(self):
#
#
#     def generer_numero(self):
#         return random.randint(10000, 99999)
#
#     @property
#     def numero(self):
#         return self._numero
#
#     @numero.setter
#     def numero(self, value):
#         if not isinstance(value, int):
#             raise ValueError("Le numéro du compte doit être un entier.")
#         self._numero = value
#
#     @property
#     def date_ouverture(self):
#         return self._date_ouverture
#
#     @date_ouverture.setter
#     def date_ouverture(self, value):
#         if not isinstance(value, date):
#             raise ValueError("La date d'ouverture doit être un objet date.")
#         self._date_ouverture = value
#
#     @property
#     def solde(self):
#         return self._solde
#
#     @solde.setter
#     def solde(self, value):
#         if not isinstance(value, (int, float)):
#             raise ValueError("Le solde doit être un nombre.")
#         self._solde = value
#
#     def crediter(self, montant):
#         self.solde += montant
#
#     def debiter(self, montant):
#         if montant > self.solde:
#             raise SoldeInsuffisantException("Solde insuffisant pour effectuer le retrait.")
#         self.solde -= montant
#
#
# class Client:
#     def __init__(self, numero=None):
#         if numero is None:
#             numero = self.generer_numero_client()
#         self.numero = numero
#         self.date_adhesion = date.today()
#         self.comptes = []
#
#     def generer_numero_client(self):
#         return random.randint(1000, 9999)
#
#     @property
#     def numero(self):
#         return self._numero
#
#     @numero.setter
#     def numero(self, value):
#         if not isinstance(value, int):
#             raise ValueError("Le numéro du client doit être un entier.")
#         self._numero = value
#
#     def equals(self, other):
#         return isinstance(other, Client) and self.numero == other.numero
#
#
# class ClientPhysique(Client):
#     def __init__(self, nom, date_naissance, numero=None):
#         super().__init__(numero)
#         self.nom = nom
#         self.date_naissance = date_naissance
#
# # Exemple d'utilisation
# compte1 = Compte()
# compte2 = Compte(solde=1000.0)
#
# client1 = Client()
# client2 = ClientPhysique(nom="John Doe", date_naissance="1990-01-01")
#
# print(f"Compte 1 - Numéro: {compte1.numero}, Solde: {compte1.solde}")
# print(f"Compte 2 - Numéro: {compte2.numero}, Solde: {compte2.solde}")
#
# print(f"Client 1 - Numéro: {client1.numero}")
# print(f"Client 2 - Numéro: {client2.numero}, Nom: {client2.nom}, Date de naissance: {client2.date_naissance}")
# obj=Compte()
# print(obj)


