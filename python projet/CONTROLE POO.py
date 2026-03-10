from abc import ABC, abstractmethod


class Véhicule(ABC):

    def __init__(self, asm, prix):
        self.matricule = None
        self.anneé_modéle = asm
        self.prix = prix
        Véhicule.increment_matricule()

    @property
    def getmatricule(self):
        return self._matricule

    # @matricule.setter
    def setmatricule(self, M):
        self._matricule = M

    @property
    def getanne(self):
        return self._anneé_modéle

    # @anneé_modéle.setter
    def setanné(self, A):
        self.__anneé_modéle = A

    @property
    def getprix(self):
        return self.__prix

    # @prix.setter
    def setprix(self, P):
        self.__prix = P

    @abstractmethod
    def demarrer(self):
        pass

    @abstractmethod
    def accelerer(self):
        pass

    def __str__(self):
        return f"Matricule: {self.__matricule} / Année du modèle: {self.__anneé_modéle}"
                f"/ Prix: {self.__prix} DH"

    @classmethod
    def increment_matricule(cls):
        if not hasattr(cls, '_matricule_counter'):
            cls._matricule_counter = 0
        cls._matricule_counter += 1

        if cls._matricule_counter < 10:
            cls._matricule_prefix = '00'
        elif cls._matricule_counter < 100:
            cls._matricule_prefix = '0'
        else:
            cls._matricule_prefix = ''

        cls._matricule_format = f"{cls._matricule_prefix}{cls._matricule_counter}"


class Voiture(Véhicule):
    def demarrer(self):
        print("Voiture démarrée.")

    def accelerer(self):
        print("Voiture en accélération.")


class Camion(Véhicule):
    def demarrer(self):
        print("Camion démarré.")

    def accelerer(self):
        print("Camion en accélération.")

# VH=[]
# def AjouterVéhicule():
#     matricule=input("donner une matricule : ")
#     an_m=int(input("donner année de module : "))
#     prix=float(input("donner prix : "))
#     VHC=Véhicule(matricule,an_m,prix)
#     VH.append(VHC)
# def chercher(numero):
#     for x in VH:
#         if (x.nbrVéhicules== numero):
#             return x
# def afficher():
#     for i in VH:
#         print(i)
# def supprimez(code):
#     if chercher(code):
#         VH.remove(chercher(code))
#         print("suppression eféctué")
#     else:
#         print("ce stagiaire n'existe pas")
#
#
# while(True):
#     print("Menu des commandes:")
#     print("1.Ajouter une véhicule")
#     print("2.Chercher une véhicule")
#     print("3.Afficher tout les véhicules")
#     print("4.Supprimer une véhicule")
#     print("5.Quitter")
#     print("Tapper le N° de votre choix :")
#     x=int(input())
#     if x==1:
#         AjouterVéhicule()
#     elif x==2:
#         n=int(input(("Donner le N°VHC à chercher :")))
#         if chercher(n):
#             print(chercher(n))
#         else:
#             print("Aucun Stagiaire avec ce N°")
#     elif x==3:
#         afficher()
#     elif x==4:
#         d=int(input("donner le N°stg à Supprimer :"))
#         supprimez(d)
#     elif x==5:
#         break
#     else:
#         print("Donner un choix entre 1 et 6")


# from abc import ABC, abstractmethod
#
#
# class Vehicule(ABC):
#     def __init__(self, annee_modele, prix):
#         self.matricule = None  # Will be set during initialization
#         self.annee_modele = annee_modele
#         self.prix = prix
#         Vehicule.increment_matricule()
#
#     @property
#     def matricule(self):
#         return self._matricule
#
#     @matricule.setter
#     def matricule(self, value):
#         self._matricule = value
#
#     @property
#     def annee_modele(self):
#         return self._annee_modele
#
#     @annee_modele.setter
#     def annee_modele(self, value):
#         self._annee_modele = value
#
#     @property
#     def prix(self):
#         return self._prix
#
#     @prix.setter
#     def prix(self, value):
#         self._prix = value
#
#     @abstractmethod
#     def demarrer(self):
#         pass
#
#     @abstractmethod
#     def accelerer(self):
#         pass
#
#     def __str__(self):
#         return f"Matricule: {self.matricule} / Année du modèle: {self.annee_modele} / Prix: {self.prix}"
#
#     @classmethod
#     def increment_matricule(cls):
#         if not hasattr(cls, '_matricule_counter'):
#             cls._matricule_counter = 0
#         cls._matricule_counter += 1
#
#         if cls._matricule_counter < 10:
#             cls._matricule_prefix = '00'
#         elif cls._matricule_counter < 100:
#             cls._matricule_prefix = '0'
#         else:
#             cls._matricule_prefix = ''
#
#         cls._matricule_format = f"{cls._matricule_prefix}{cls._matricule_counter}"
#
#
# class Voiture(Vehicule):
#     def demarrer(self):
#         print("Voiture démarrée.")
#
#     def accelerer(self):
#         print("Voiture en accélération.")
#
#
# class Camion(Vehicule):
#     def demarrer(self):
#         print("Camion démarré.")
#
#     def accelerer(self):
#         print("Camion en accélération.")
#
#
# # Test Program
# if __name__ == "__main__":
#     voiture1 = Voiture(2022, 25000)
#     print(voiture1)
#
#     camion1 = Camion(2021, 50000)
#     print(camion1)
#
#     voiture1.demarrer()
#     voiture1.accelerer()
#
#     camion1.demarrer()
#     camion1.accelerer()



#________________________Vnew______________________
# from abc import ABC, abstractmethod
#
#
# class Vehicule(ABC):
#     V=0
#     def __init__(self, annee_modele, prix):
#         Vehicule.V +=1
#         self.__matricule = Vehicule.V
#         self.__annee_modele = annee_modele
#         self.__prix = prix
#
#     def matricule(self):
#         return self.__matricule
#
#     def matricule(self, value):
#         self.__matricule = value
#
#
#     def annee_modele(self):
#         return self.__annee_modele
#
#     def annee_modele(self, value):
#         self.__annee_modele = value
#
#
#     def prix(self):
#         return self.__prix
#
#
#     def prix(self, value):
#         self.__prix = value
#
#
#     def demarrer(self):
#         pass
#
#
#     def accelerer(self):
#         pass
#
#
#     def __str__(self):
#         return f"Matricule: {self.matricule} / Année du modèle: {self.annee_modele} / Prix: {self.prix}"
#
#
#
#
#
# class Voiture(Vehicule):
#     def __init__(self,annee_modele, prix):
#         super().__init__(self,annee_modele, prix)
#
#     def matricule(self):
#         return self.__matricule
#
#     def matricule(self, value):
#         self.__matricule = value
#
#
#     def annee_modele(self):
#         return self.__annee_modele
#
#     def annee_modele(self, value):
#         self.__annee_modele = value
#
#
#     def prix(self):
#         return self.__prix
#
#
#     def prix(self, value):
#         self.__prix = value
#
#     def demarrer(self):
#         print("Voiture démarrée.")
#
#     def accelerer(self):
#         print("Voiture en accélération.")
#
#     def _str_(self):
#          x = super()._str_()
#          return f"{x}"
#
# class Camion(Vehicule):
#
#     def __init__(self, annee_modele, prix):
#         super().__init__(self, annee_modele, prix)
#
#     def matricule(self):
#         return self.__matricule
#
#     def matricule(self, value):
#         self.__matricule = value
#
#     def getannee_modele(self):
#         return self.__annee_modele
#
#     def setannee_modele(self, value):
#         self.__annee_modele = value
#
#     def getprix(self):
#         return self.__prix
#
#     def setprix(self, value):
#         self.__prix = value
#     ans=property(getannee_modele(),setannee_modele())
#     px=property(getprix(),setprix())
#     def demarrer(self):
#         print("Voiture démarrée.")
#
#     def accelerer(self):
#         print("Voiture en accélération.")
#
#     def _str_(self):
#         x = super()._str_()
#         return f"{x}"
#     def demarrer(self):
#         print("Camion démarré.")
#
#     def accelerer(self):
#         print("Camion en accélération.")
#     def __str__(self):
#         x=super().__str__()
#         return f"{x}"
#
# # Test Program
# if __name__ == "__main__":
#     voiture1 = Voiture(2022, 25000)
#     print(voiture1)
#
#     camion1 = Camion(2021, 50000)
#     print(camion1)
#
#     voiture1.demarrer()
#     voiture1.accelerer()
#
#     camion1.demarrer()
#     camion1.accelerer()

#____________________version2____________________

from abc import ABC, abstractmethod


class vehicule(ABC):
    c = 0

    def _init_(self, l, p):
        vehicule.c += 1
        self.__matricule = vehicule.c
        self.__lannee_module = l
        self.__prix = p

    def get_annemod(self):
        return self.__lannee_module

    def set_annemod(self, nombre):
        self.__lannee_module = nombre

    def get_prix(self):
        return self.__prix

    def set_prix(self, nombre):
        self.__prix = nombre

    lannee_module = property(get_annemod, set_annemod)
    prix = property(get_prix, set_prix)

    def demarrer(self):
        pass

    def accelerer(self):
        pass

    def _str_(self):
        return (
            f"matricule: {self.__matricule} "
            f"l anne de module: {self.__lannee_module} "
            f"prix: {self.__prix} "
        )


class voiture(vehicule):
    def _init_(self, annemod, pr):
        super()._init_(annemod, pr)

    def get_annemod(self):
        return self.__lannee_module

    def set_annemod(self, nombre):
        self.__lannee_module = nombre

    def get_prix(self):
        return self.__prix

    def set_prix(self, nombre):
        self.__prix = nombre

    annemod = property(get_annemod, set_annemod)
    pr = property(get_prix, set_prix)

    def demarrer(self):
        print("cest un message de class voiture")

    def accelerer(self):
        print("cest un message de classe voiture")

    def _str_(self):
        x = super()._str_()
        return f"{x}"


class camions(vehicule):
    def _init_(self, anmod, prix_cam):
        super()._init_(anmod, prix_cam)

    def get_anmod(self):
        return self.__lannee_module

    def set_anmod(self, nombre):
        self.__lannee_module = nombre

    def get_prix_cam(self):
        return self.__prix

    def set_prix_cam(self, nombre):
        self.__prix = nombre

    anmod = property(get_anmod, set_anmod)
    prix_cam = property(get_prix_cam, set_prix_cam)

    def demarrer(self):
        print("cest un message de class camoins")

    def accelerer(self):
        print("cest un message de classe camoins")

    def _str_(self):
        x = super()._str_()
        return f"{x}"


# teste le programme___________________________________________________________________
# _objet voiture________________________________
v1 = voiture(2020, 90000)
v1.lannee_module = 2024
v1.prix = 50000
print(v1)
v1.demarrer()
v1.accelerer()

# _objet camoins________________________________
cam1 = camions(2001, 150000)
cam1.lannee_module = 1997
cam1.prix = 66666
print(cam1)
cam1.demarrer()
cam1.accelerer()