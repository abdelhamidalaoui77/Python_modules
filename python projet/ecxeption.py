#------------------------------- Exception NOTES ----------------------------------------------------


# class InvalidNoteError(Exception):
#     def __init__(self, note, message="Note invalide. Veuillez entrer une note entre 0 et 20."):
#         self.note = note
#         self.message = message
#         Exception.__init__(self, self.message)
#
#
# # Fonction pour traiter la note
# def process_grade_input():
#     while True:
#         try:
#             user_input = float(input("Veuillez entrer votre note (entre 0 et 20) : "))
#             process_grade(user_input)
#             print("Note valide !")
#             break  # Sortir de la boucle si l'entrée est valide
#         except ValueError:
#             print("Erreur : Veuillez entrer un nombre.")
#         except InvalidNoteError as e:
#             print(f"Erreur : {e}")
#
#
# # Fonction pour vérifier la note
# def process_grade(note):
#     if not 0 <= note <= 20:
#         raise InvalidNoteError(note)
#
#
# # Appel de la fonction pour traiter l'entrée de l'utilisateur
# process_grade_input()
#
#
#
#
#
#
#
# class NameError(Exception):
#     def __init__(self, name, message="Invalide. Veuillez utiliser uniquement des lettres avec ou sans espace."):
#         self.name = name
#         self.message = message
#         Exception.__init__(self, self.message)
#
# def  process_name_input():
#     while True:
#         try:
#             A = input("Veuillez entrer votre nom : ")
#             NOM_PRENOM_verification(A)
#             print("Nom valide !")
#             break
#         except NameError as e:
#             print(f"Erreur : {e}")
#
# def process_firstname_input():
#     while True:
#         try:
#             user_input = input("Veuillez entrer votre prénom : ")
#             NOM_PRENOM_verification(user_input)
#             print("Prénom valide !")
#             break
#         except NameError as e:
#             print(f"Erreur : {e}")
#
#
# # Fonction pour vérifier le nom ou prénom
# def process_name(name):
#     if not name.replace(" ", "").isalpha():
#         raise NameError(name)
#
#
# def NOM_PRENOM_verification(name):
#     if not name.replace(" ", "").isalpha():
#         raise NameError(name)
#
# process_name_input()
# process_firstname_input()

# class Employe:
#     c=0
#     def __init__(self,nom_emp,salaire,grade):
#         Employe.c  += 1
#         self.code_emp = Employe.c
#         self.nom = nom_emp
#         self.salaire = salaire
#         self.grade = grade
#     def __str__(self):
#         return f"{self.nom} N°{self.code_emp} : {self.salaire} DH {self.grade}"
#
#
# class Chef(Employe):
#     def __init__(self,nom_emp,salaire,grade,service,liste_emp):
#         Employe.__init__(self,nom_emp,salaire,grade)
#         self.service = service
#         self.employes = []
#     def __str__(self):
#         # lempC = [f"{j.nom}  {j.salaire} DH {j.grade}" for j in self.employes]
#         return f"{self.nom} {self.salaire} {self.grade} {self.service}"  #- Liste Employe : {lempC}"
# Lemp=[]
# def ajout():
#     nom_emp=input("donner un nom :")
#     while True:
#         try:
#             salaire=float(input("donner un salaire :"))
#             break
#         except ValueError:
#             print("le salaire doit étre en des chiffres")
#
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
#
# while(True):
#     print("Menu des commandes:")
#     print("1.Ajouter un Employe")
#     print("2.Chercher un Employe")
#     print("3.Afficher tout les Employes")
#     print("4.Supprimer un Employe")
#     print("5.exporter vers un fichier")
#     print("6.Quitter")
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
#         exporter()
#     elif x==6:
#         break
#     else:
#         print("Donner un choix entre 1 et 6")
# def chercheremploye(code):
#     for i in Lemp:
#         if x.code_emp ==code:
#             return x
# C=[]
# service_chef=input("donner une service :")
# nom=input("d: ")
# salaire=int(input("sa : "))
# grad=input("do: ")
# x=int(input("donner le nombre de employes a ajouter: "))
# print(Lemp)
# for i in range(x):
#     while True:
#         num=int(input("donner le code a ajouter:"))
#         if Recherche(num) and Recherche(num)not in Lemp:
#             C.append(Recherche(num))
#             break
#
# cf=Chef(service_chef,nom,salaire,grad,C)
# print(cf)

#______________ex1__________
# l=[]
# for i in range(10):
#     i=int(input("donner l'entier :"))
#     l.append(i)
# print("la somme de liste",sum(l))
# print("la moyenne de liste",sum(l)/10)
# l.sort()
# print(l)
# print("le max de liste",max(l))
# print("max :",l[-1])
# print("la min de liste",min(l))
# print("min :",l[0])
# #__________________ex2________
# def SommeDiv(n):
#     s=0
#     for i in range(1,n):
#         if n % i ==0:
#             s+=i
#     return s
# n=0
# while n<=0:
#     n=int(input("donne un entier positif :"))
# x=SommeDiv(n)
# if  x==n:
#     print(n,"est parfait")
# else:
#     print(n,"non parfait")
#________________ex3____________
def symetrique(liste):
    c=0
    if len(liste) % 2 ==0 :
         for i in liste:
             if liste[i] == liste[-i-1]:
                 c+=1
             if c==len(liste)/2:
                 return True
             else:
                  return False
    else:
        return False
l=[1,2,3,3,2,1]
print(symetrique(l))
#____________ex4________
# f=open("fichier.txt","r")
# print(f.readline())
# print(f.readline())
# f.close()