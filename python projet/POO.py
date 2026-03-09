#-----------------------------declaration de la class---------------------
# class stagiaire:
#     def __init__(self,p_nom,p_prenom): #constrecteur avec deux parametres
#         self.nom = p_nom
#         self.prenom = p_prenom
#         self.note = []
#     def moyenne(self):
#         return sum(self.note)/len(self.note)
#
#     def afficher(self):
#         print(self.nom, self.prenom, self.moyenne(), sep="")

#
# #--------------------------------------------------------------------------
# class Stagiaire:
#     def __init__(self, p_nom, p_prenom,num_ins):
#         self.nom = p_nom
#         self.prenom = p_prenom
#         self.notes = []
#         self.num=num_ins
#         self.nstagaire=[]
#
#     def Moyenne(self):
#         return sum(self.notes) / len(self.notes)
#
#     def DemanderNotes(self, nombre_notes):
#         for i in range(nombre_notes):
#             note = float(input(f"Entrez la note {i + 1}: "))
#             self.notes.append(note)
#
#     def Afficher(self):
#         print(f"{self.nom} {self.prenom} - Moyenne: {self.Moyenne()}")
#     def ajouter(self):
#         n=int(input("donner le nombre de stagiairs"))

# Stg = Stagiaire("yassin", "zakari")
# n=int(input("donner le nombre de notes a entrer : "))
# Stg.DemanderNotes(n)
# Stg.Afficher()
#____________________________
#____________________________

# class Stagiaire:
#     def __init__(self, p_nom, p_prenom,num_ins):
#         self.notes = []


# n=int(input("donner le nombre de stagiare:"))
# l = []
# for i in range(n):
#    s=(input("donner le nom complet de stagiare: "))
#    id=input("de 1 a infinte: ")
#    x=str(s)+" "+str(id)
#    l.append(x)
# print(l)



# class stagiare
#
# l=[]
# def ajoutestagiare:             ajout d'un slg des l
#     s=stagiare(_______)
#     s.notes.append(______)
#     l.append(s)
# def afichetouslesstagiare:
#  foreach stg in l:
#     stg.AL
# class Stagiaire:
#    def __init__(self, p_nom, p_prenom, p_num):
#       self.nom = p_nom
#       self.prenom = p_prenom
#       self.num = p_num
#       self.notes = []
#
#    def moyenne(self):
#       return sum(self.notes) / len(self.notes)
#
#    def demander_notes(self):
#       nombre_notes = int(input("Donner le nombre de notes à entrer : "))
#       for i in range(nombre_notes):
#          note = float(input(f"Entrez la note {i + 1}: "))
#          self.notes.append(note)
#
#
#
#    def __str__(self):
#       return f"{self.nom} {self.prenom} {self.num} - Moyenne: {self.moyenne()}"
#
#
# l = []
#
#
# def ajouter_stagiaire():
#    nom = input("Nom : ")
#    prenom = input("Prenom : ")
#    num = int(input("Num D'inscription : "))
#    stg = Stagiaire(nom, prenom, num)
#    stg.demander_notes()
#    l.append(stg)
#
#
# def afficher_stagiaires():
#    for i in l:
#       print(i)
#
#
# def chercher_stagiaire(numero):
#    for x in l:
#       if x.num == numero:
#          return x
#
#
# def moyenne_generale():
#    total = 0
#    for x in l:
#       total += x.moyenne()
#
#    moyenne_gen = total / len(l)
#    return moyenne_gen
#
#
# n = int(input("Donner le nombre de stagiaires : "))
# for i in range(n):
#    ajouter_stagiaire()
# num = int(input("donner le num d'inscription a chercher : "))
# if chercher_stagiaire(num):
#    print("stagiaire num", num, " :", chercher_stagiaire(num))
# else:
#    print("Aucun stagiaire trouvé avec ce num d'inscription.")
#
# num2 = int(input("donner le num d'inscription du stagiaire a supprimer : "))
# if chercher_stagiaire(num2):
#    l.remove(chercher_stagiaire(num2))
#    print("stagiaire num ", num2, "est supprime")
# else:
#    print("Aucun stagiaire trouvé avec ce num d'inscription.")
#
# print("Affichage de tout les stagiaires : ")
# afficher_stagiaires()
#
# print("moyenne generale : ", moyenne_generale())

#--------------------------------------------------------------------------------------------------------
# class Stagiaire:
#    def __init__(self, p_nom, p_prenom, p_num):
#       self.nom = p_nom
#       self.prenom = p_prenom
#       self.num = p_num
#       self.notes = []
#
#    def __str__(self):
#       return f"{self.nom} {self.prenom} {self.num}-{self.moyenne}"
#
#    def moyenne(self):
#       return sum(self.notes) / len(self.notes)
#
# l = []
#
#
# def ajouter_stagiaire():
#    nom = input("Nom : ")
#    prenom = input("Prenom : ")
#    num = int(input("Num D'inscription : "))
#    stg = Stagiaire(nom, prenom, num)
#    n=int(input("donner le nombre des notes a entrer:"))
#    for i in range(n):
#       stg.notes.append(float(input("Entrez la note "+str(i+1)+":")))
#    l.append(stg)
#
#
# def afficher_stagiaires():
#    for x in l:
#       print(x)
#
#
# def chercher_stagiaire(numero):
#    for x in l:
#       if x.num == numero:
#          return x
#
#
#
#
# def suppstg(numero):
#    if chercher_stagiaire(numero):
#       l.remove(chercher_stagiaire(numero))
#       print("suppression effectue")
#    else:
#       print("aucun stagiaire avec ce numero")
#
#
#
#
# T=True
# while(T):
#    print("1.Ajouter un stagiaire")
#    print("2.chercher un stagiaire")
#    print("3.Afficher ")
#    print("4.Supprimer un stagiaire")
#    print("5.arreter")
#    print("tappez le nombre de votre choix:")
#    x=int(input())
#    if x==1:
#       ajouter_stagiaire()
#    elif x==2:
#       print("donner le num a chercher:")
#       num=int(input())
#       if chercher_stagiaire(num):
#          print("stagiaire num", num, " :", chercher_stagiaire(num))
#       else:
#          print("ce numero n'existe pas" )
#    elif x==3:
#       afficher_stagiaires()
#    elif x==4:
#       d=int(input(("donner le numero a supprimer:")))
#       suppstg(d)
#    elif x==5:
#       T=False
#    else:
#       print("dooner un choix entre 1 et 5")
#
#

class stagiaire:

   def __init__(self, p_nom, p_prenom,p_num):
      self.nom = p_nom
      self.prenom = p_prenom
      self.num = p_num
      self.notes = []

   def moyenne(self):
      return sum(self.notes) / len(self.notes)

   def __str__(self):
      return f"{self.nom} {self.prenom} {self.num} {self.notes}- Moyenne: {self.moyenne()}"


l = []


def Ajoutstg():
   nom = input("Nom : ")
   prenom = input("Prenom : ")
   num = int(input("Num D'inscription : "))
   while chercher_stg(num):
      num = int(input("Donner un autre N° : "))
   stg = stagiaire(nom, prenom, num)
   n = int(input("Donner le nombre de notes à entrer : "))
   for i in range(n):
      stg.notes.append(float(input(f"Entrez la note {i + 1}: ")))
   l.append(stg)


def chercher_stg(numero):
   for x in l:
      if x.num == numero:
         return x
def chercherindice(n):
    for i in range(len(l)):
        if l[i].num==n:
            return i
    return -1


def afficher_stg():
   for i in l:
      print(i)

def modifier(x):
    indice=chercherindice(x)
    if indice==-1:
        print("ce num n'existe pas")
    else:
        l[indice].nom = input("dooner le nouveau nom:")
        l[indice].prenom = input("dooner le nouveau prenom:")
        l[indice].num = int(input("dooner le nouveau num:"))
def supp_stg(xnum):
   if chercher_stg(xnum):
      l.remove(chercher_stg(xnum))
      print("suppression éffectuée")
   else:
      print("Aucun Stagiaire avec ce num")

def exporterdonneé():
    f=open("stagiaire.txt","w")
    for stagiaire in l:
        f.writelines(f"{(stagiaire)}\n")
D = []
def importe(fichier):
    with open("stagiaire.txt","r")as file:
        lignes = fichier.readlines()
        for ligne in lignes:
            donnes_stagiaires = ligne.split()
            nom = donnes_stagiaires[0]
            prenom = donnes_stagiaires[1]
            num = int(donnes_stagiaires[2])
            notes = [float(note) for note in donnes_stagiaires[3:]]
            stg = stagiaire(nom, prenom, num)
            stg.notes = notes
            D.append(stg)


while (True):
   print("1.Ajouter un Stagiaire")
   print("2.Chercher un Stagiaire")
   print("3.Afficher tout les Stagiaires")
   print("4.Supprimer un Stagiaire")
   print("5.modifier un stagiaire")
   print("6.exporter vers un fichier")
   print("7.importer depuis un fichier")
   print("8.Quitter")
   print("Tapper le N° de votre choix :")
   x = int(input())
   if x == 1:
      Ajoutstg()
   elif x == 2:
      n = int(input(("Donner le N°stg à chercher :")))
      if chercher_stg(n):
         print(chercher_stg(n))
      else:
         print("Aucun Stagiaire avec ce N°")
   elif x == 3:
      afficher_stg()
   elif x == 4:
      d = int(input("donner le N°stg à Supprimer :"))
      supp_stg(d)
   elif x==5:
       n=int(input("donner un indice :"))
       modifier(n)
   elif x==6:
       exporterdonneé()
   elif x==7:
       importe(fichier)
   elif x == 8:
       break
   else:
      print("Donner un choix entre 1 et 8")

# --------------------------------------Version 3------------------------------------------------------
# class stagiaire:
#     n = 1
#     def __init__(self, p_nom, p_prenom):
#         self.nom = p_nom
#         self.prenom = p_prenom
#         self.num = stagiaire.n
#         self.notes = []
#         stagiaire.n+=1
#     def moyenne(self):
#         return sum(self.notes) / len(self.notes)
#
#     def __str__(self):
#         return f"{self.nom} {self.prenom} {self.num} - Moyenne: {self.moyenne()}"
#     def infoclass():
#         print("je suis classe stagiaire")
#
#
# l = []
#
# def Ajoutstg():
#     nom = input("Nom : ")
#     prenom = input("Prenom : ")
#     stg = stagiaire(nom, prenom)
#     a = int(input("Donner le nombre de notes à entrer : "))
#     for i in range(a):
#         stg.notes.append(float(input(f"Entrez la note {i + 1}: ")))
#     l.append(stg)
#
# def chercher_stg(numero):
#     for x in l:
#         if x.num == numero:
#             return x
#
# def afficher_stg():
#     for i in l:
#         print(i)
#
# def supp_stg(xnum):
#     if chercher_stg(xnum):
#         l.remove(chercher_stg(xnum))
#         print("suppression éffectuée")
#     else:
#         print("Aucun Stagiaire avec ce num")
#
#
#
#
#
#
# while(True):
#     print("nombre des objets:",stagiaire.n)
#     print("1.Ajouter un Stagiaire")
#     print("2.Chercher un Stagiaire")
#     print("3.Afficher tout les Stagiaires")
#     print("4.Supprimer un Stagiaire")
#     print("5.Quitter")
#     print("Tapper le N° de votre choix :")
#     x=int(input())
#     if x==1:
#         Ajoutstg()
#     elif x==2:
#         n=int(input(("Donner le N°stg à chercher :")))
#         if chercher_stg(n):
#             print(chercher_stg(n))
#         else:
#             print("Aucun Stagiaire avec ce N°")
#     elif x==3:
#         afficher_stg()
#     elif x==4:
#         d=int(input("donner le N°stg à Supprimer :"))
#         supp_stg(d)
#     elif x==5:
#         break
#     else:
#         print("Donner un choix entre 1 et 6")