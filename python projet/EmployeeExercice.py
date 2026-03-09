class Employer:
    n = 0

    def __init__(self, nom_emp, salaire, grade):
        self.nom = nom_emp
        self.salaire = salaire
        self.grade = grade
        Employer.n += 1
        self.code = Employer.n

    def __str__(self):
        return f" code : {self.code} / nom : {self.nom} / salaire : {self.salaire} DH / grade : {self.grade}"


class Chef(Employer):
    def __init__(self, nom_emp, salaire, grade, service):
        self.service = service
        self.liste_emp = []
        super().__init__(nom_emp, salaire, grade)



    def __str__(self):
        chef_info = super().__str__()
        employees_info = "\n".join([f"  - {emp}" for emp in self.liste_emp])
        return f"{chef_info} / Service: {self.service} / Liste des employés:{employees_info}"

class InvalidNameError(Exception):
    def __init__(self, nom, message="Invalide. Veuillez utiliser uniquement des lettres avec ou sans espace."):
        self.nom = nom
        self.message = message
        super().__init__(self.message)


# Fonction pour traiter le nom
def process_name_input():
    while True:
        try:
            noms = input("Veuillez entrer un nom : ")
            NOM_PRENOM_verification(noms)
            return noms
        except InvalidNameError as e:
            print(f"Erreur : {e}")


def NOM_PRENOM_verification(nom):
    if not nom.replace("", "").isalpha():
        raise InvalidNameError(nom)


lemp = []


def ajouter_emp():
    nom = process_name_input()
    while True:
        try:
            salaire = float(input("salaire : "))
            break
        except ValueError:
            print("Veuillez saisir que des chiffres !!")

    grade = input("grade : ")
    stg = Employer(nom, salaire, grade)
    lemp.append(stg)


def afficher_emp():
    for i in lemp:
        print(i)


def chercher_emp(numero):
    for x in lemp:
        if x.code == numero:
            return x


def supp_stg(xnum):
    if chercher_emp(xnum):
        lemp.remove(chercher_emp(xnum))
        print("suppression éffectuée")
    else:
        print("Aucun employer avec ce num")


def exportfichier():
    while True:
        try:
            with open("Fichier1.txt", "w") as file:
                for x in lemp:
                    file.writelines(f"{x}\n")
            break
        except FileNotFoundError:
            print("fichier introuvable !!")

C=[]

def ajouteChefetempForchef():
    n = process_name_input()
    while True:
        try:
            s = float(input("Donner salaire de chef : "))
            break
        except ValueError:
            print("Veuillez saisir que des chiffres !!")
    g = input("donner grade de chef : ")
    service = input("donner la service de chef: ")
    stg = Chef(n, s, g, service)
    listeemployees = []
    nombre = int(input("Donner le nombre de employees a ajouter :"))
    for i in range(nombre):
        while True:
            code = int(input("donner le code du employee : "))
            emp = chercher_emp(code)
            if emp and emp not in listeemployees:
                listeemployees.append(emp)
                break
    stg.liste_emp = listeemployees
    C.append(stg)

def afichechef():
    for x in C:
        print(x)
while True:
    print("1.Ajouter un employer")
    print("2.Chercher un employer")
    print("3.Afficher tout les employers")
    print("4.Supprimer un employer")
    print("5.export dans un fichier")
    print("6.mouvez to noveaux menu")
    print("Tapper le N° de votre choix :")
    x = int(input())
    if x == 1:
        ajouter_emp()
    elif x == 2:
        x = int(input("donner le num a chercher:"))
        if chercher_emp(x):
            print(chercher_emp(x))
        else:
            print("Aucun Stagiaire avec ce N°")
    elif x == 3:
        afficher_emp()
    elif x == 4:
        d = int(input("donner le N°stg à Supprimer :"))
        supp_stg(d)
    elif x == 5:
        exportfichier()
    elif x == 6:
        break
    else:
        print("Donner un choix entre 1 et 6")
while True:
    print("menu des commandes: ")
    print("1.ajouter chdf et ses employes")
    print("2.affichage de chef et ses employes")
    print("3.arreter le programe")
    choix=int(input("donner le nombre de votre choix: "))
    if choix == 1:
        ajouteChefetempForchef()
    elif choix == 2:
        afichechef()
    elif choix == 3:
        break
    else:
        print("veuillez entrer un nombre entr 1 et 3")
