#------------------------Ex1 ----------------------------------
# def SupprimeDoublon(maliste):
#     l=[]
#     for x in maliste :
#         if x not in l:
#             l.append(x)
#     return l
#
# L1 = []
# print("Remplissage de nouvelle liste")
# rep = "oui"
# while rep == "oui":
#     L1.append(int(input("Donner un entier :")))
#     print("Voulez-vous ajouter un autre entier ? Oui/Non")
#     rep = input()
#     rep = rep.lower()
# print(SupprimeDoublon(L1))

#---------------------Ex2--------------------------------
# stock = ["Ordinateur de bureau","Ordinateur portable",100,"Camera",310.28,"Haut-Parleurs",27.00
#     ,"Télevision",1000,"Cartes mères","souris","clavier",500,"barettes de mémoire"]
# print(stock)
# l1=[]
# l2=[]
# for x in stock:
#     if type(x)==str:
#         l1.append(x)
#     else:
#         l2.append(x)
# print("liste 1 : ",l1)
# print("liste 2 : ",l2)
# print("taille liste 1 :",len(l1))
# print("taille liste 2 :",len(l2))
# print("Ordre Croissant :")
# l2.sort()
# l1.sort()
# print(l2)
# print(l1)
# print("Ordre Décroissant :")
# l2.reverse()
# l1.reverse()
# print(l2)
# print(l1)

#-------------------------------Ex3------------------------------------
# f=open("myFile.txt","w")
# for i in range(1,6):
#     f.writelines("Ligne numero"+str(i)+"\n")
# f.close()
# f=open("myFile.txt","r")
# lignes = f.readlines()
# lignes[2]= "desole! le contenu de cette ligne a ete change!\n"
# f.close()
# f=open("myFile.txt","w")
# f.writelines(lignes)
# f.close()

#-----------------------------Ex5--------------------------------------
# with open("info.txt","r") as f:
#     text = f.read()
#     words = text.split()
#     loguest_word =max(words,key=len)
#     print("le plus long : ",loguest_word)

#-------------------------------Ex6---------------------------------
# f1=open("fichier1.txt","r")
# f2=open("fichier2.txt","r")
# l = []
# text1 = f1.read()
# text2 = f2.read()
# words1 = text1.split()
# words2 = text2.split()
# for x in words1:
#     if x in words2 and x not in l :
#         l.append(x)
# print(l)

#------------------------Ex7--------------------------------------
# f=open("myFile2.txt","w")
# f.writelines(["Python Programming\n","Java Programming\n","C++ Programming\n"])
# f.close()
# f=open("myFile2.txt","r")
# lignes = f.readlines()
# lignes[2],lignes[1]=lignes[1],lignes[2]
# f.close()
# f=open("myFile2.txt","w")
# f.writelines(lignes)
# f.close()

#------------------------Ex8----------------------------------------
# f=open("fichier1.txt","r")
# print(f.readlines())
# def lire_premieres_lignes(nom_fichier, n):
#     with open(nom_fichier, 'r') as fichier:
#         lignes = fichier.readlines()
#         premieres_lignes = [ligne.strip() for ligne in lignes[:n]]
#     return premieres_lignes
#
# def lire_dernieres_lignes(nom_fichier, n):
#     with open(nom_fichier, 'r') as fichier:
#         lignes = fichier.readlines()
#         dernieres_lignes = [ligne.strip() for ligne in lignes[-n:]]
#     return dernieres_lignes
#
# def extraire_et_enregistrer(nom_fichier_source, nom_fichier_destination):
#     with open(nom_fichier_source, 'r') as fichier_source:
#         lignes = fichier_source.readlines()
#         if len(lignes) >= 5:
#             contenu_extrait = lignes[2:5]
#             with open(nom_fichier_destination, 'w') as fichier_destination:
#                 fichier_destination.writelines(contenu_extrait)
#             print(f"Contenu extrait et enregistré dans {nom_fichier_destination}")
#         else:
#             print("Le fichier source n'a pas suffisamment de lignes.")
#
# fichier = "myFile.txt"
# n_premieres=int(input("donner le nombre des premieres lignes a lire : "))
# print(lire_premieres_lignes(fichier,n_premieres))
# n_dernieres=int(input("donner le nombre des dernieres lignes a lire : "))
# print(lire_dernieres_lignes(fichier,n_dernieres))
#
# fichier_2=input("donner un fichier : ")
# extraire_et_enregistrer(fichier,fichier_2)
#------------------------
#-------EFM--------------
# def symetrique(maliste):
#     l1=[]
#     l2=[]
#     for x in range(0,len(maliste)/2):
#         l1.append(x)
#     for y in range(len(maliste)-1,(len(maliste)/2)-1,-1):
#         l2.append(y)
#     l2.reverse()
#     c=0
#     for i in l1:
#         for j in l2:
#             if l1[i]==l2[j]:
#                 c+=1
#     if c==len(maliste)/2:
#         return True
#     else:
#         return False
# l = []
# rep="OUI"
# while (rep=="OUI"):
#   l.append(int(input("Donner une valeur:")))
#   print("voullez vous ajoutez une autre valeure?OUI/NON:")
#   rep=input()
#   rep=rep.upper()
# if symetrique(l)==True:
#         print("la liste est symetrique")
# else:
#         print("la liste pas symetrique")
# def symetrique(maliste):
#     l1=[]
#     for x in range(len(maliste)/2):
#         l1.append(x)
#     return l1
# l=[1,2,3,4,5,6]
# print(symetrique(l))
# def symetrique(liste):
#     for i in range(len(liste)):
#         if liste[i]==liste[-i-1]:
#             return  True
#         else:
#             return False
# l=[1,2,3,4,4,3,2,1]
# print(symetrique(l))


class Joueur:
    codejoueur = 0

    def _init_(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        Joueur.codejoueur += 1
        self.num = Joueur.codejoueur

    def _str_(self):
        return f"{self.nom} {self.prenom} {self.age} -Code joueur : {self.num}"


LJ = []


def ajouter_joueurs():
    nom = input("Donner le nom de joueur : ")
    prenom = input("donner le prenom de joueur : ")
    age = int(input("Donner l'age du joueur : "))
    obj1 = Joueur(nom, prenom, age)
    LJ.append(obj1)


def supprimer_joueurs(numero):
    for i in LJ:
        if i.num == numero:
            LJ.remove(i)

    for index, i in enumerate(LJ, start=1):
        i.num = index


def modifier_nom_prenom(numero):
    choix_nom = " "
    while choix_nom != "oui" and choix_nom != "non":
        choix_nom = input(("Voulez-vous modifier le nom ( Oui ) ou ( Non ):")).lower()

    if choix_nom == "oui":
        for i in LJ:
            if i.num == numero:
                new_first_name = input("donner un nouveau nom :")
                i.nom = new_first_name
    else:
        pass

    choix_prenom = " "
    while choix_prenom != "oui" and choix_prenom != "non":
        choix_prenom = input(("Voulez-vous modifier le prenom (Oui ou Non) : ")).lower()

    if choix_prenom == "oui":
        for i in LJ:
            if i.num == numero:
                new_last_name = input("donner un nouveau prenom : ")
                i.prenom = new_last_name
    else:
        pass


def afficher_joueurs():
    for i in LJ:
        print(i)


class Equipe():
    codeequipe = 0

    def _init_(self, nom_equipe):
        self.nom = nom_equipe
        self.listejoueurs = []
        Equipe.codeequipe += 1
        self.num = Equipe.codeequipe

    def afficher_listejoueurs(self):
        x = " "
        for i in self.listejoueurs:
            x = x + (str(i) + "  ")
        return x

    def _str_(self):
        return f"{self.nom}  [{self.afficher_listejoueurs()}]  -Code Equipe: {self.num}"


def chercher_joueur(code):
    for i in LJ:
        if i.num == code:
            return i


LE = []


def ajouter_equipe():
    nom = input("Donner le nom d'equipe :")
    nombre_joueur = int(input("donner le nombre de joueur que voulez-vous ajouter :"))
    objEquipe = Equipe(nom)
    for i in range(nombre_joueur):
        code = int(input("donner le code de joueur:"))
        if chercher_joueur(code):
            objEquipe.listejoueurs.append(chercher_joueur(code))
    LE.append(objEquipe)


def afficher_equipe():
    for i in LE:
        print(i)


def supprimer_equipe(code_equipe):
    for i in LE:
        if i.num == code_equipe:
            LE.remove(i)

    for index, i in enumerate(LE, start=1):
        i.num = index


def modifier_nom_equipe(code_equipe):
    for i in LE:
        if i.num == code_equipe:
            new_name = input("Donner un nouveau nom :")
            i.nom = new_name


while True:
    print("1-Ajouter Joueur")
    print("2-Afficher Joueur")
    print("3-Modifier Nom | Prenom")
    print("4-Supprimer Joueur")
    print("5.Exporter Joueurs vers un fichier texte")
    print("6.Importer Joueurs depuis un fichier texte")
    print("7-Ajouter Equipe")
    print("8-Afficher Equipe")
    print("9-Modifier le Nom d'Equipe")
    print("10-Supprimer Equipe")
    print("11.Exporter Equipes vers un fichier texte")
    print("12.Importer Equipes depuis un fichier texte")
    print("13-Quitter")
    choix = int(input("choisissez un nombre entre 1-13 :"))

    if choix == 1:
        ajouter_joueurs()

    elif choix == 2:
        afficher_joueurs()

    elif choix == 3:
        numero = int(input("donner le numero de joueur que vous voulez modifier :"))
        modifier_nom_prenom(numero)

    elif choix == 4:
        numero = int(input("donner le numero de joueur que vous voulez supprimer : "))
        supprimer_joueurs(numero)

    elif choix == 5:
        f = open("Joueurs.txt", "w")
        for i in LJ:
            f.write(str(i) + "\n")

    elif choix == 6:
        f = open("Joueurs.txt", "r")
        line = f.readlines()
        f.close()
        for i in line:
            rep = i.split()
            nom, prenom, age, num = rep[0], rep[1], rep[2], rep[6]
            obj1 = Joueur(nom, prenom, age)
            obj1.num = num
            LJ.append(obj1)

    elif choix == 7:
        ajouter_equipe()

    elif choix == 8:
        afficher_equipe()

    elif choix == 9:
        code_equipe = int(input("donner le code d'equipe que voulez-vous changer son nom :"))
        modifier_nom_equipe(code_equipe)

    elif choix == 10:
        code_equipe = int(input("donner le code d'equipe que voulez-vous supprimer :"))
        supprimer_equipe(code_equipe)

    elif choix == 11:
        f = open("Equipes.txt", "w")
        for i in LE:
            f.write(str(i) + "\n")

    elif choix == 12:
        f = open("Equipes.txt", "r")
        line = f.readlines()
        f.close()

        for i in line:
            rep = i.split()
            nom, numero = rep[0], rep[-1]
            obj1 = Equipe(nom)
            obj1.num = numero

            nom, prenom, age, num = rep[2], rep[3], rep[4], rep[8]
            obj2 = Joueur(nom, prenom, age)
            obj2.num = num
            obj1.listejoueurs.append(obj2)

            LE.append(obj1)

    elif choix == 13:
        break

    else:
        print("veuillez choisissez un nombre entre 1-13:")