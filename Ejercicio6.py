import os
os.system("cls")

"desarrolle el programa que determine la edad menor y mayor de tres edades ingresadas"

edad=input("escribir número de edades:")
edad_int=int(edad)
if edad_int>=18:
    print("Es mayor de edad")
else:
    print("es menor de edad")
