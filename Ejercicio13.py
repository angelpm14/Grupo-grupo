import os
os.system("cls")
'''Ingresa numero de 3 cifras'''
print("")
n = int(input("ingresar"))

n1 = int (input("primer numero"))
n2 = int (input("segundo numero"))
n3 = int (input("tercer numero"))

if n1 < n2 < n3 :
    print("estan ordenados de forma creciente")
else:
    print("estan ordenados de forma descendente")