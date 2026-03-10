class Joueur:
    codejoueur = 0

    def _init_(self, nom: str, prenom: str, age: int):
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
