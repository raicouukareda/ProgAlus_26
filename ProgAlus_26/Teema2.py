# # if lause
# from multiprocessing import Value


# try:
#     x = int(input("Sisesta arv: "))
#     if x > 0:
#      print("Positiivne arv")
#      print("See rida on ka if-i sees")
#      print("See rida täidetakse alati")
# except ValueError:
#     print("Sisesta number")

# #if...else lause
# try:
#     x = int(input("Sisesta arv: "))
#     if x == 1:
#         print("Õige")
#     else:
#         print("Vale")
# except ValueError:
#     print("Sisesta number")

# #tingimised

# vastus = input("Kas soovid jätkata? (jah/ei) ")
# if vastus.lower() == "jah":
#     print("Jätkame!")
# else:
#     print("Head aega!")

# #elif (sama mis elseif lua-st?)

# try:
#     x = int(input("Sisesta arv -5 kuni 5: "))
#     if x < -5:
#         print("Vähe")
#     elif -5 <= x <= 5:
#         print("OK")
#     else:
#         print("Palju")
# except ValueError:
#     print("Sisesta number")

#plokkskeem pythoniks

try:
    summa = float(input("summa: "))
    if summa > 2000:
        hind = summa * 0.8
    elif summa > 1000:
        hind = summa * 0.9
    else:
        hind = summa
    print("Hind:", hind)
except ValueError:
    print("sisesta numberino")
