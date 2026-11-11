from math import *

#Ülesanne 1

from datetime import *
tana = date.today()

print(f"Tere! Täna on {tana}")

tana1 = tana.strftime("%d/%m/%Y")
print(tana1)

tana2 = tana.strftime("%B %d, %Y")
print(tana2)

tana3 = tana.strftime("%m/%d/%y")
print(tana3)

tana4 = tana.strftime("%b-%d-%Y")
print(tana4)

aasta = tana.year
kuu = tana.month
paev = tana.day
print(f"Tänane aasta: {aasta}, kuu: {kuu}, päev: {paev}")

kuulõpuni = date(aasta, kuu+1, 1) - tana
aastalõpuni = date(aasta+1, 1, 1) - tana
print(f"Jäänud päevi kuu lõpuni: {kuulõpuni.days}")
print(f"Jäänud päevi aasta lõpuni: {aastalõpuni.days}")

# Ülesanne 2

print("Tehe 3 + 8 / (4 - 2) * 4 =", 3 + 8 / (4 - 2) * 4)

# Ülesanne 3

try:
    R = float(input("Sisesta ringi raadius R: "))
    ruudu_pindala = (2*R)**2
    ruudu_ümbermõõt = 4*(2*R)
    ringi_pindala = 3.14*R**2
    ringi_ümbermõõt = 2*3.14*R
    print(f"Ruudu pindala: {ruudu_pindala}, \nruudu ümbermõõt: {ruudu_ümbermõõt}, \nringi pindala: {ringi_pindala}, \nringi ümbermõõt: {ringi_ümbermõõt}")
except ValueError:
    print("Sisesta kehtiv arv")

# Ülesanne 4

maa_raadius = 6378 #km
mundi_dia = 2 #cm
mundi_raadius = mundi_dia/2 #cm
maa_ümber = 2*pi*maa_raadius*1000 #cm
mundi_arv = maa_ümber/mundi_dia
print(f"2-euroseid münte on vaja: {mundi_arv:.0f}")

y=10
x=3
v=x % y
print(v)