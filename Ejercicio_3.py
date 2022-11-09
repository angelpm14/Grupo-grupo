import os
os.system("cls")

grados = int(input("Ingrese numero de grados: "))
minutos = int(input("Ingrese numero de minutos: "))
segundos = int(input("Ingrese numero de segundos: "))

beta = grados + minutos / 60.0 + segundos / 3600.0

if beta == 0:
    print("Nulo")
elif beta <90:
    print("Agudo")
elif beta == 90:
    print("Recto")
elif beta < 180:
    print("Obtuso") 
elif beta == 180:
    print("Llano")