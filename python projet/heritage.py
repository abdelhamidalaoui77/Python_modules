# class bird:
#     def intro(self):
#         print("theres are many types of birds")
#     def flight(self):
#         print("most of birds can fly but some cannot fly")
# class sparraw(bird):
#     def flight(self):
#         print("sparraws can fly")
# class ostrich(bird):
#     def flight(self):
#         print("ostriches cannot fly")
# obj_bird= bird()
# obj_sparraw=sparraw()
# obj_ostrich= ostrich()
# obj_bird.intro()
# obj_bird.flight()
# obj_sparraw.intro()
# obj_sparraw.flight()
# obj_ostrich.intro()
# obj_ostrich.flight()
# #------------------------------------------------
# class grandfather:
#     def __init__(self,grandfathername):
#         self.grandfathername=grandfathername
#     def __str__(self):
#         return f"grandfather:{self.grandfathername}"
# class father(grandfather):
#     def __init__(self,fathername,grandfathername):
#         self.fathername=fathername
#         grandfather.__init__(self, grandfathername)
#     def __str__(self):
#         return f" father:{self.fathername},{self.grandfathername} "
# father_obj = father("hamid","yasin")
# print(father_obj)


class Bachelier:
    c=0
    def __init__(self,Nom,Prenom,moyenne):
        self.nom = Nom
        self.prenom = Prenom
        self.moyenne = moyenne
        Bachelier.c+=1
        self.CNE = Bachelier.c
    def mention(self):
        if self.moyenne < 10:
            return "Non validé"
        elif self.moyenne >= 10 and self.moyenne < 12:
            return "passable"
        elif self.moyenne >= 12 and self.moyenne < 14:
            return "assez bien"
        elif self.moyenne >= 14 and self.moyenne < 16:
            return " bien"
        elif self.moyenne >= 16 and self.moyenne < 18:
            return "excellent"
    def __str__(self):
        return f"bachelier {(self.CNE)} : {self.nom} {self.prenom} Moyenne: {self.moyenne}  {self.mention()}"


class stagiaire(Bachelier):
    n=0
    def __init__(self,Nom,Prenom,moyenne):
        stagiaire.n += 1
        self.numins = stagiaire.n
        Bachelier.__init__(self, Nom,Prenom,moyenne)
        self.module=[]
    def Moy(self):
        return sum(self.module)/len(self.module)
    def Dnotes(self):
        Nnotes=int(input("donner le nombre des notes a ajouter: "))
        for i in range(Nnotes):
            note=float(input(f"donner la note {i + 1}: "))
            self.module.append(note)

    def mentionS(self):
        if self.Moy() < 10:
            return "Non validé"
        elif self.Moy() >= 10 and self.Moy() < 12:
            return "passable"
        elif self.Moy() >= 12 and self.Moy() < 14:
            return "assez bien"
        elif self.Moy() >= 14 and self.Moy() < 16:
            return " bien"
        elif self.Moy() >= 16 and self.Moy() < 18:
            return "trés bien"
        elif self.Moy() >= 18 :
            return "excellent"

    def __str__(self):

        return f" stagiaire CNE: {self.CNE} , numeroinscription {self.numins}: {self.nom} {self.prenom} MoyBac :{self.moyenne} moyenne: {self.Moy()} {self.mentionS()}"
class NoteException(Exception):
    pass
def VNotes(note):
    if note < 0 or note > 20:
        raise NoteException("la note doit etre comprise entre 0 et 20")


LS=[]
def Ajouterstagiaire():
    nom=input("nom : ")
    prenom=input("prenom : ")
    moyenne=float(input("moyenne : "))
    try:
        VNotes(moyenne)
    except NoteException as e:
        print(e)


    stg=stagiaire(nom,prenom,moyenne)
    stg.Dnotes()
    LS.append(stg)
def chercher(numero):
    for x in LS:
        if x.numins == numero:
            return x
def afficher():
    for i in LS:
        print(i)
def supprimez(code):
    if chercher(code):
        LS.remove(chercher(code))
        print("suppression eféctué")
    else:
        print("ce stagiaire n'existe pas")


while(True):
    print("Menu des commandes:")
    print("1.Ajouter un Stagiaire")
    print("2.Chercher un Stagiaire")
    print("3.Afficher tout les Stagiaires")
    print("4.Supprimer un Stagiaire")
    print("5.Quitter")
    print("Tapper le N° de votre choix :")
    x=int(input())
    if x==1:
        Ajouterstagiaire()
    elif x==2:
        n=int(input(("Donner le N°stg à chercher :")))
        if chercher(n):
            print(chercher(n))
        else:
            print("Aucun Stagiaire avec ce N°")
    elif x==3:
        afficher()
    elif x==4:
        d=int(input("donner le N°stg à Supprimer :"))
        supprimez(d)
    elif x==5:
        break
    else:
        print("Donner un choix entre 1 et 6")
#____________________________________________________________________



#_________________________________________________________

# BR=input("anneé de naissance: ")
# try:
#     print('tu as',2024-int(BR),'ans.')
# except:
#     print('erreur')
# print("fin de progreamme")
# try:
#     a=int(input("a?: "))
#     b=int(input("b? :"))
#     print(a,'/',b, '=', a/b)
# except Exception as e:
#     print(type(e))
#     print(e)

# try:
#     a=int(input("a?: "))
#     b=int(input("b? :"))
#     print(a,'/',b, '=', a/b)
# except ValueError:
#     print('erruer de conversation.')
# except ZeroDivisionError:
#     print('division par zéro.')
# except:
#     print('autre errueur')


# def fact(n):
#     if n < 0:
#         raise ArithmeticError()
#     if n == 0:
#         return 1
#     return n * fact(n-1)
# # print(fact(-12))
# try:
#     n = int(input("entrer un nombre:"))
#     print(fact(n))
# except ArithmeticError:
#     print("veuillez entrer un nombre positif.")
# except:
#     print("veuillez entrer un nombre.")

# class NoRootException(Exception):
#     pass
#
# from  math import sqrt
#
# def trinomialroots(a,b,c):
#     delta = b ** 2 - 4 * a * c
#     # aucune racine réelle
#     if delta < 0 :
#         raise NoRootException()
#     # un racine réelle double
#     if delta ==0:
#         return -b (2 * a)
#     #Deux racines réelles simples
#     x1 = (-b + sqrt(delta)) / (2 * a)
#     x2 = (-b - sqrt(delta)) / (2 * a)
#     return (x1, x2)
#
# try:
#     print(trinomialroots(-1, 4, 2))
# except NoRootException:
#     print("pas de racine réelle.")
# #Pas de racine réelle





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