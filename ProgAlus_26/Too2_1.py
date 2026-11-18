# # Ülesanne 1


# eesnimi = input("mis on eesnimi? ")

# if eesnimi.lower() == "juku":
#     print("lähme jukuga kinno")
#     if eesnimi == "JUKU":
#         print("ära karju")
#     vanus = input("kui vana? ")
#     if vanus.isdigit():
#         vanus = int(vanus)
#         if vanus < 6:
#             pilet = "tasutapilet"
#         elif 6 <= vanus <= 14:
#             pilet = "lastepilet"
#         elif 15 <= vanus <=65:
#             pilet = "täispilet"
#         elif vanus >= 65:
#             pilet = "sooduspilet"
#         else:
#             print("mingi viga")
#         print(f"juku on {vanus} aastat vana, seega vaja võtta {pilet}")
#     else:
#         print("see pole vanus")
# else:
#     print("kinno ei lähe")


# # Ülesanne 2

# pinginaaber1 = input("sisesta esimene nimi: ")
# pinginaaber2 = input("sisesta teine nimi: ")

# print(f"Tere {pinginaaber1.capitalize()} ja {pinginaaber2.capitalize()}")
# if pinginaaber1.isalpha() and pinginaaber2.isalpha():
#     if pinginaaber1 in ["Joonas", "Kenneth"] and pinginaaber2 in ["Joonas", "Kenneth"]:
#         print(f"Inimesed {pinginaaber1.capitalize()} ja {pinginaaber2.capitalize()} on täna pinginaabrid")
#     else:
#         print("Inimesed ei ole täna pinginaabrid")
# else:
#     print("sisesta nimed õigesti !!!!!")


# # Ülesanne 3

# pikkus = float(input("mis on selle ristkülikukujulise ruumi pikkus? "))
# laius = float(input("mis on selle ristkülikukujulise ruumi laius? "))
# pindala = pikkus*laius
# print(f"toa pindala on {pindala} ruutmeetrit")
# remont = input("kas remonti soovite teha? (jah/ei) ")
# if remont.lower() == "jah":
#     rm_hind=float(input("sisesta ruutmeetri hind: "))
#     remont_hind = pindala*rm_hind
#     print(f"põranda vahetamise hind on {remont_hind} eurot")
#     prof=input("kas kasutad professionaali abi? (jah/ei) ")
#     if prof.lower() == "jah":
#         too_hind=float(input("sisesta töö hind ruutmeetri kohta: "))
#         koguhind = remont_hind + (pindala*too_hind)
#         print(f"remondi koguhind koos tööga on {round(koguhind,2)} eurot")
# else:
#     print("remonti ei tehta")


# # Ülesanne 4

# try:
#     alghind = float(input("mis on selle toode alghind? "))
#     if alghind > 700:
#       hind = alghind * 0.7
#     else:
#       hind = alghind
#     print(f"toode hind on {round(hind,2)} eurot")
# except ValueError:
#     print("hind peaks olema numbrites")

# # Ülesanne 5

# try:
#     temperatuur = float(input("sisesta temperatuur kraadides: "))
#     if temperatuur > 18:
#         print("Toatemperatuur on üle 18 kraadi")
#     else:
#         print("Toatemperatuur on 18 kraadi või madalam")
# except ValueError:
#     print("kraadid peaks olema numbrites")

# Ülesanne 6

# try:
#     pikkus = float(input("sisesta humanoid pikkus (cm): "))
#     if  30 <= pikkus < 160:
#         print("inimene on lühike")
#     elif 160 <= pikkus <= 180:
#         print("inimene on keskmine pikkusega")
#     elif 180 < pikkus <= 220:
#         print("inimene on pikk")
#     else:
#         print("pikkus pole sobilik")
# except ValueError:
#     print("palun sisesta pikkus numbrina")

# # Ülesanne 7 (ül. 6 aga nüüd küsib ka sugu)

# sugu = input("sugu: ")
# if sugu.isalpha():
#     if sugu.lower()=="m" or sugu.upper()=="MEES":
#         print("mehe pikkuse analüüs")
#         try:
#             pikkus = float(input("sisesta humanoid pikkus (cm): "))
#             if  30 <= pikkus < 160:
#                 print("inimene on lühike")
#             elif 160 <= pikkus <= 180:
#                 print("inimene on keskmine pikkusega")
#             elif 180 < pikkus <= 220:
#                 print("inimene on pikk")
#             else:
#                 print("pikkus pole sobilik")
#         except ValueError:
#             print("tähtedega pole võimalik, number vaja")
#     else:
#         print("naise pikkuse analüüs")
#         try:
#             pikkus = float(input("sisesta humanoid pikkus (cm): "))
#             if  30 <= pikkus < 150:
#                 print("inimene on lühike")
#             elif 150 <= pikkus <= 170:
#                 print("inimene on keskmine pikkusega")
#             elif 170 < pikkus <= 210:
#                 print("inimene on pikk")
#             else:
#                 print("pikkus pole sobilik")
#         except ValueError:
#             print("tähtedega pole võimalik, number vaja")
# else:
#     print("täht paluks")

# Ülesanne 8

from random import *
summa = 0
arve = "Toode   Kogus   Hind    Kokku\n"
valik = input("kas soovid osta piima? (jah/ei): ")
if valik.lower()=="jah":
    kogus = input("mitu piima tahaksid võtta? (int): ")
    if kogus.isdigit():
        kogus = int(kogus)
        p_hind = round(uniform(0.5, 3.6),2)
        print(f"piima hind on {p_hind}€")
        summa += round(kogus*p_hind,2)
        print(f"piima kogusumm on {summa}€")
        arve+=f"piim    {kogus}       {p_hind}€   {round(kogus*p_hind,2)}€\n"
    else:
        print("midagi läks valesti")
else:
    print("ok siis piima ei osta")

valik = input("kas soovid osta leiba? (jah/ei): ")
if valik.lower()=="jah":
    kogus = input("mitu leiba tahaksid võtta? (int): ")
    if kogus.isdigit():
        kogus = int(kogus)
        l_hind = round(uniform(1.5, 3.5),2)
        print(f"leiva hind on {l_hind}€")
        summa += round(kogus*l_hind,2)
        print(f"leiva kogusumm on {summa}€")
        arve+=f"leib    {kogus}       {l_hind}€   {round(kogus*l_hind,2)}€\n"
    else:
        print("midagi läks valesti")
else:
    print("ok siis leiba ei osta")

print("Arve nr. 123456789")
print(arve)