import numpy
from numpy import array
N= 0
while N<= 0:
    N=int(input("donner le nombre de stagaires:"))
T= array([int]*N)
for i in range (0,N-1):
    T[i]=-1
    while T[i]<0 or T[i]>20:
        T[i]=int(input("donner la note de stagiaire",i+1,":"))
print("les notes sont:")
for i in range (0,N-1):
        print(T[i])