from math import * #valesti pandud
print("Ruudu karakteristikud")
a=float(input('Sisesta ruudu külje pikkus => ')) #float
S=a**2
print("Ruudu pindala", S)
P=4*a
print("Ruudu ümbermõõt", P) #erinevad märgid " '
di=a*sqrt(2) #math polnud vaja
print("Ruudu diagonaal", round(di,2))
#print() <- see print ei pea olema
print("Ristküliku karakteristikud") #lisa sulg )
b=float(input("Sisesta ristküliku 1. külje pikkus => ")) #float
c=float(input("Sisesta ristküliku 2. külje pikkus => ")) #float
S=b*c
print('Ristküliku pindala', S) #puudus ' märk
P=2*(b+c) #korrutamis märk *
print("Ristküliku ümbermõõt", P)
di=sqrt(b*2+c*2) #math polnud vaja
print("Ristküliku diagonaal", round(di)) #puudus sulg )
print()
print("Ringi karakteristikud")
r=float(input('Sisesta ringi raadiusi pikkus => ')) #kaks ' märki, peaks olema kas üks ' mark või " , pidi olema ka float
d=2*r #puudus * märk
print("Ringi läbimõõt", d) #puudus koma
S=pi*r*2 #sulge polnud vaja
print("Ringi pindala", round(S))
C=2*pi*r #puudus * märk, sulge polnud vaja
print("Ringjoone pikkus", round(C)) #puudus sulg )