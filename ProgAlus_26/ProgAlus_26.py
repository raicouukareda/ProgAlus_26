print("Hello world!")

print("Ma õpin",1,". kursusel") #sa tead väga hästi mida tavaline print teeb dingus
print("Aasta on",2026)

kursus=1 #int
aasta=2026 #int

print("Ma õpin",kursus,". kursusel")
print("Aasta on",aasta)

print("Aastal",aasta+1,"olen juba",kursus+1,". kursusel")

print("2026", "10", "01", sep="-") #sep="-" määrab, mis eraldub väljastatavaid väärtusi
print("Sama ", end="") #end="\n" määrab, mis pannakse lõppu, vaikmisi on see reavahetus
print("rida")

#Sisendamine
nimi=input("Sisesta oma nimi: ") #input on funkstioon, mis võimaldab kasutajal sisestada väärtust
print("Tere",nimi,"!")

#Teised andmetüübid
a = input("Esimene arv: ") #str 17->"17"
b = input("Teine arv: ") #str 
print(a + b)

a = int(input("Esimene arv: ")) #int("17")->17, float 17.0->17.0
b = int(input("Teine arv: "))
print(a + b)

#Põhioperatsioonid
print("Liitmine: ")
a = float(input("Esimene arv: "))
b = float(input("Teine arv: "))
print(a,"+",b,"=", a + b)

print("Lahutamine: ")
a = 7float(input("Esimene arv: "))
b = float(input("Teine arv: "))
print(a,"-",b,"=", a - b)

print("Korrutamine: ")
a = float(input("Esimene arv: "))
b = float(input("Teine arv: "))
print(a,"*",b,"=", a * b)

print("Jagamine: ")
a = float(input("Esimene arv: "))
b = float(input("Teine arv: "))
print(a,"/",b,"=", a / b)

print("Astendamine: ")
a = float(input("Esimene arv: "))
b = float(input("Teine arv: "))
print(a,"**",b,"=", a ** b)

print("Jagamise täisarvuline osa: ")
a = float(input("Esimene arv: "))
b = float(input("Teine arv: "))
print(a,"//",b,"=", a // b)

print("Jagamisjääk: ")
a = float(input("Esimene arv: "))
b = float(input("Teine arv: "))
print(a,"%",b,"=", a % b)

#Tõeväärtused
p = True
q = False
print(not p, p and q, p or q)
print(5 > 3 and 2 > 4) #->False
print(5 > 3 or 2 > 4) #->True

#Formatimine
nimi = "Raico"
punktid = 87
print(f"{nimi} sai {punktid} punkti.")

hind = 19.9
kogus = 3
print(f"Kokku: {hind * kogus:.2f} eurot") #ümardab kahe komakohani

#Matemaatlised funktsioonid
import math

print("Pii väärtus:", math.pi) #Pii väärtus
print("√16 =", math.sqrt(16)) #Ruutelement
print("sin(π/2) =", math.sin(math.pi / 2)) #Sin
print("sin(30°) =", round(math.sin(math.radians(30)), 2)) #Sin
print("5! =", math.factorial(5)) #Faktoriaal (1*2*3*4*5=120)