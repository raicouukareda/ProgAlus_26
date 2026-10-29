#Töö 1.1

#NR.1

nimi = input("sisesta enda nimi: ")
vanus = int(input("sisesta enda vanus: ")) #int() teisendab stringi täisarvuks

print(f"Tere, maailm! Tervitan sind {nimi}! Te olete {vanus} aastat vana.")

#NR.2

vanus = 18 #int
eesnimi = "Jaak" #str
pikkus = 16.5 #float
kas_käib_koolis = True #bool

print(f"Muutuja: {vanus}, tüüp: {type(vanus)}")
print(f"Muutuja: {eesnimi}, tüüp: {type(eesnimi)}")
print(f"Muutuja: {pikkus}, tüüp: {type(pikkus)}")
print(f"Muutuja: {kas_käib_koolis}, tüüp: {type(kas_käib_koolis)}")


#NR.3

from random import * #randint

kommide_arv = randint(100, 200)

print(f"Laual on {kommide_arv} kommi")

try:
  ära_võtta = int(input("Mitu kommi tahad laualt ära võtta? > "))
  print(f"Sa võtsid laualt {ära_võtta} kommi. Laual on nüüd {kommide_arv - ära_võtta} kommi alles")
except:
    print("??? bro")

#NR.4

from math import * #pi, sqrt (nr.5-ks)

ümbermõõt = float(input("Mis on puu ümbermõõt? > "))

läbimõõt = ümbermõõt / pi

print(f"Puu läbimõõt on {läbimõõt}")

#NR.5

N = float(input("Sisesta ristküliku 1. külje pikkus: "))
M = float(input("Sisesta ristküliku 2. külje pikkus: "))
d = sqrt(N**2+M**2)
print(f"Ristküliku diagonaal on {d}")

#NR.6

aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus / aeg

print("Sinu kiirus oli " + str(kiirus) + " km/h")

#NR.7

arv1 = int(input("esimene arv: "))
arv2 = int(input("teine arv: "))
arv3 = int(input("kolmas arv: "))
arv4 = int(input("neljas arv: "))
arv5 = int(input("viies arv: "))

keskmine = (arv1+arv2+arv3+arv4+arv5)/5
summa = arv1+arv2+arv3+arv4+arv5

print(f"Arvude summa on: {summa}")
print(f"Arvude keskmine on: {keskmine}")

täisosa = summa//5
jääk = summa%5

print(f"Täisosa on: {täisosa}")
print (f"Jääk on: {jääk}")

#NR.8

print("    @..@")
print("   (----)")
print("  ( \__/ )")
print('  ^^ "" ^^ ')

#NR.9

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

P = a+b+c

print(f"Kolmnurga ümbermõõt on: {P}")

