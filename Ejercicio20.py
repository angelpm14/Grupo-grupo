import os
os.system("cls")
'''Determinar el orden ascendente de 3 numeros'''
print("")
n = int(input("ingresar"))

a = int(input("ingresar primer numero"))
b = int(input("ingresar segundo numero"))
c = int(input("ingresar tercer numero"))

if a < b < c :
    print("Estan ordenandos de forma ascendente")
elif a > b > c :
    print("Estan ordenados de forma descendente")
else:
    print("Estan desordenados")