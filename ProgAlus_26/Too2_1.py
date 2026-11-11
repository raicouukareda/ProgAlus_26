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
