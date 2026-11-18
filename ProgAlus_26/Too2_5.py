print("Vali programm:\n1 - Aastaaeg\n2 - Kiiruse kontroll\n3- Taksosõit")
try:
    valik=int(input("sisesta valik (1-3) => "))
    if valik == 1:
        print()
        print("Aastaaeg") # siin oli kaks erinevat märki, " ja ', tegin mõlemad " märgiks
        kuu=int(input("Sisesta kuu number (1-12) => "))
        if kuu<1 and kuu>12:
            print("Vigane kuu")
        elif kuu==12 or kuu<=2: # ainult üks võrdusmärk (kuu=12), lisasin ühe veel (kuu==12)
            print("Talv")
        elif 3<=kuu<=5: # ei saa olla 'else if', peab olema 'elif', muutsin 'elif'iks
            print("Kevad")
        elif 6<=kuu<=8: # koolon : puudus
            print("Suvi") # ei olnud vahe 'print' ees, lisasin TAB vahemik
        else:
            print("Sügis")

    elif valik == 2:
        print()
        print("Kiiruse kontroll")
        lubatud=int(input("Sisesta lubatud kiirus (km/h) => ")) # sulg puudus, lisasin
        kiirus=int(input("Sisesta tegelik kiirus (km/h) => ")) # lisasin 'int' kuna järgmine rida ilma selleta ei toimuks
        if lubatud > 0 or kiirus > 0:
            yletus=kiirus-lubatud
            if yletus<=0: # < ja = märgid olid tagurpidi, panin õigesti
                    print("Kiirust ei ületatud")
            elif 1 <= yletus <= 19: # muutsin selle 1-19, kuna isegi kui yletus on üle 100, ikka annab hoiatus
                    print("Hoiatus")
            elif 20 <=yletus <= 39: # sama põhjus mis eelmises
                    print("Trahv")
            else: # muutsin 'else'iks, kuna elif yletus<40 ei prindinud välja järgmist rida
                    print("Juhiluba võetakse ära")
        else:
            print("negatiivsed arvud ei saa")

    elif valik == 3:
        print()
        print("Taksosõit")
        km=float(input("Sisesta sõidu pikkus (km) => "))
        oo=input("Kas sõit on öösel (jah/ei)? => ")
        hind=3+km+0.8
        if oo=="jah" and oo=="JAH": # puudus koolon :
            hind=hind*1.2
        if km > 50:
            hind=hind*0.9
        print("Sõidu hind:", round(hind,2), "€") # sulg puudus, lisasin

    else:
        print("see pole õige valik")
except ValueError:
    print("sisesta arv, et valida programmi")








# print("Aastaaeg") # siin oli kaks erinevat märki, " ja ', tegin mõlemad " märgiks
# kuu=int(input("Sisesta kuu number (1-12) => "))
# if kuu<1 and kuu>12:
#     print("Vigane kuu")
# elif kuu==12 or kuu<=2: # ainult üks võrdusmärk (kuu=12), lisasin ühe veel (kuu==12)
#     print("Talv")
# elif 3<=kuu<=5: # ei saa olla 'else if', peab olema 'elif', muutsin 'elif'iks
#     print("Kevad")
# elif 6<=kuu<=8: # koolon : puudus
#     print("Suvi") # ei olnud vahe 'print' ees, lisasin TAB vahemik
# else:
#     print("Sügis")
# print()
# print("Kiiruse kontroll")
# lubatud=int(input("Sisesta lubatud kiirus (km/h) => ")) # sulg puudus, lisasin
# kiirus=int(input("Sisesta tegelik kiirus (km/h) => ")) # lisasin 'int' kuna järgmine rida ilma selleta ei toimuks
# yletus=kiirus-lubatud
# if yletus<=0: # < ja = märgid olid tagurpidi, panin õigesti
#     print("Kiirust ei ületatud")
# elif 1 <= yletus <= 19: # muutsin selle 1-19, kuna isegi kui yletus on üle 100, ikka annab hoiatus
#     print("Hoiatus")
# elif 20 <=yletus <= 39: # sama põhjus mis eelmises
#     print("Trahv")
# else: # muutsin 'else'iks, kuna elif yletus<40 ei prindinud välja järgmist rida
#     print("Juhiluba võetakse ära")
# print()
# print("Taksosõit")
# km=float(input("Sisesta sõidu pikkus (km) => "))
# oo=input("Kas sõit on öösel (jah/ei)? => ")
# hind=3+km+0.8
# if oo=="jah" and oo=="JAH": # puudus koolon :
#     hind=hind*1.2
# print("Sõidu hind:", round(hind,2), "€") # sulg puudus, lisasin
