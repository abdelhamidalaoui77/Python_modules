# import numpy 
# from numpy import array
# N= 0
# while N<= 0:
#     N=int(input("donner le nombre de stagaires:"))
# T= numpy.array([int]*N)
# for i in range (0,N):
#     T[i]=-1
#     while T[i]<0 or T[i]>20:
#         T[i]=int(input("donner la note de stagiaire"+str(i+1)+":"))
# print("les notes sont: ")
# for i in range (0,N-1):
# print(T[i])

# import numpy
# from numpy import array
# N=0
# while N<=0:
#     N=int(input("Donner le nombre des stagaires :"))
# T=array([float]*N)
# for i in range(0,N):
#     T[i]=-1
#     while T[i]<0 or T[i]>20:
#         T[i]= int(input("Donner la note N"+str(i+1)+":"))
# max=T[0]
# for i in range(0,N):
#     if T[i]>T[0]:
#         max=T[i]
# print("la note maximale est:",max)

# import numpy
# from numpy import array
# N=0
# while N<=0:
#     N=int(input("Donner le nombre des stagaires :"))
# T=array([float]*N)
# for i in range(0,N):
#     T[i]=-1
#     while T[i]<0 or T[i]>20:
#         T[i]= int(input("Donner la note N"+str(i+1)+":"))
# max=T[0]
# min=T[0]
# for i in range(0,N):
#     if T[i]>T[0]:
#         max=T[i]
#     if T[i]<T[0]:
#         min=T[i]
# print("la note maximale:",max)
# print("la note minimale:",min)
#
# import numpy
# from numpy import array
# N=0
# while N<=0:
#     N=int(input("Donner le nombre des stagaires :"))
# T=array([float]*N)
# s=0
# for i in range(0,N):
#     T[i]=-1
#     while T[i]<0 or T[i]>20:
#         T[i]= int(input("Donner la note N"+str(i+1)+":"))
#     s+=T[i]
#     if i==0:
#         max=T[i]
#         min=T[i]
#     else:
#      if T[i]>max:
#       max=T[i]
#      if T[i]<min:
#       min=T[i]
# print("la note maximale est:",max)
# print("la note minimale est:",min)
# print("la moyenne generale:",s/N)


# print("")
# max=T[0]
# min=T[0]
#     if T[i]>max:
#         max=T[i]
#     if T[i]<min:
#         min=T[i]
# print("la note maximale:",max)
# print("la note minimale:",min)
# s=0
# for i in range(0,N):
#     s=s+T[i]
# print("la moyenne:"+str(s/N))
# x=0
# for i in range(0,N):
#     if T[i]>=(s/N):
#         x+=1
# print("les nombres des notes sup:",x)
# print("les nombres des notes inf",N-x)
# _________exercice1
# import numpy
# from numpy import array
# N1=int(input("donner la taille de table 1:"))
# N2=int(input("donner la taille de table 2:"))
# t1=array([int]*N1)
# t2=array([int]*N2)
# for i in range(N1):
#     t1[i]=int(input("doner la valeur"+str(i+1)+":"))
# for i in range(N2):
#     t2[i]=int(input("donner la valeur"+str(i+1)+":"))
# N3=0
# for i in range(N1):
#     for j in range(N2):
#         if t1[i]==t2[j]:
#            N3+=1
# r=0
# t3=array([int]*N3)
# for i in range(N3):
#     for j in range(N1):
#         for n in range(N2):
#             if t1[j] == t2[n]:
#                t3[i]=t1[j]
#                r+=1
#                if r<=N3:
#                  print("la table t3 est :",t3[i])
# __________0FF
def testerparfait(x):
    s=0
    for i in range(1,x):
        if (x%i==0):
            s+=i
    if (s==x):
        return 1
    else:
        return 0
for i in range(1,1001):
    if testerparfait(i)==1:
       print(i,"parfait")
# ____________exercice__________
# def produit(n):
#     x=1
#     for i in range(1,n+1):
#         x*=i
#     return x
# def somme_produit(m):
#     s=0
#     for i in range(1,m+1):
#         s+=produit(i)
#     return s
# N=int(input("donner une valeur de N:"))
# print("la solution de série f=1!+2!+3!+...+N!:",somme_produit(N))
# --------------la sommme s=1+2+3+...+N--------------
# def somme(s):
#     x=0
#     for i in range(1,s+1):
#         x+=i
#     return x

# --------------le produit-----------
# def produit(s):
#     p=1
#     for i in range(1,s+1):
#         p*=i
#     return p
# N=int(input("donner un valeur de N:"))
# print("le produit de s=1*2*3*...*N=",produit(N))
# ------------------------diviseur---------------------
# ______________________________________________________

# def diviseur(N):
#     import numpy
#     from numpy import array
#     s = 0
#     for i in range(1, N + 1):
#         if N % i == 0:
#             s += 1
#     t1 = [s]
#     for j in range(1, N + 1):
#         if N % j == 0:
#             t1[j] = j
#     for j in range(1, s + 1):
#         return t1[j]
#
#
# X = int(input("donner une X:"))
# diviseur(X)
# print("la table est {}:".format(diviseur(X)))
#________________tri----------
# def liste():
#     l=[]
#     rep="OUI"
#     while rep=="OUI":
#         l.append(int(input("donner un entier:")))
#         print("ajoute un autre entier?,Oui/Non")
#         rep=input()
#         rep=rep.upper()
#     return l
# #________tuple________
# x=("fes","beni mellal","casa",1,2,3)
# print(x)
# x=list(x)
# print(x)
# x[0]="tanger"
# x[3]=5
# x=tuple(x)
# print(x)
# t=(1,2,3)
# for x in range(len(t)):
#     print(t[x],end="")
# thisdict={"brand":"Ford","model":"Mustang","year":1964}
# for x in thisdict:
#     print(thisdict[x])
#---------EXERICE2--------
# l=[]
# rep="OUI"
# while (rep=="OUI"):
#     l.append(int(input("Donner la note:")))
#     print("voullez vous ajoutez une autre note?OUI/NON:")
#     rep=input()
#     rep=rep.upper()
# s=0
# for x in l:
#      s+=x
# m=s/len(l)
# N=[]
# for x in l:
#     if x>=m:
#         N.append(x)
# print("la moyenne generale est :",m)
# print("les notes sup:",N)
# #_______exercice3_________
# def Diviseurs(n):
#     l=[]
#     for i in range(1,n+1):
#         if n%i==0:
#             l.append(i)
#     return l
# def ElementsCommuns(L1,L2):
#         L3=[]
#         for x in L1:
#             if x in L2 and x not in L3:
#                 L3.append(x)
#         return L3
# a=int(input("donner la valeur de a:"))
# b=int(input("donner la valeur de b:"))
# a=Diviseurs(a)
# b=Diviseurs(b)
# L3=ElementsCommuns(a,b)
# print("le plus grand commun est:",max(L3))
# #----------exercice4---------
# def programme(l,a):
#     if a in l:
#         x=l.index(a)
#     if a in l:
#         return x
#     else:
#         return -1
# l=[]
# rep="OUI"
# while (rep=="OUI"):
#     l.append(int(input("Donner une valeur:")))
#     print("voullez vous ajoutez une autre valeure?OUI/NON:")
#     rep=input()
#     rep=rep.upper()
# a = int(input("donner la valeur de a:"))
# print(programme(l,a))
# #-------------ecercice5----------
# f=open("fichier.txt","r")
# print(f.read())
# f.close()
#----1----
# f=open("fichier.txt","r")
# print(f.read())
# #---2
# f =open("fichier.txt","r")
# print(f.read(10))
#f.close()
#  #---3
# f =open("fichier.txt","r")
# print(f.read()[5:10])
#f.close()
# #---4
# f =open("fichier.txt","r")
# lignes=f.readlines()
# nombre_de_ligne=len(lignes)
# print("nombres de lignes",nombre_de_ligne)
#f.close()
# #---5--------------
# f=open("fichier.txt","r")
# lignes=f.readlines()
# lignes[0]="debut\n"
# f.close()
# f =open("fichier.txt","w")
# f.writelines(lignes)
# f.close()
# #---6---------------
# f=open("fichier.txt","a")
# f.write("\nFin")
# f.close()
#-------exercice 2-----
# import shutil
# f=open("fichier2.txt","w")
# src= "fichier.txt"
# dest="fichier2.txt"
# shutil.copy

# s="example  de texte   avec des  espaces  multiple  "
# l=s.split()
# newtext=""
# for x in l:
#     newtext= newtext+x+ " "#----entre""il--ya--1--espace--"1espace"
# print(newtext)

# def est_symetrique(liste):
#     """
#     Cette fonction vérifie si une liste est symétrique en comparant les éléments de chaque côté.

#     :param liste: La liste à vérifier.
#     :return: True si la liste est symétrique, False sinon.
#     """
#     longueur = len(liste)
#     for i in range(longueur // 2):
#         if liste[i] != liste[longueur - 1 - i]:
#             return False
#     return True

# # Exemple d'utilisation
# liste1 = [1, 2, 3, 2, 1, 2]
# liste2 = [2, 2, 3, 4, 5,5 , 4 , 3  ,2, 2]

# print(est_symetrique(liste1))  # Doit retourner True
# print(est_symetrique(liste2))  # Doit retourner False

