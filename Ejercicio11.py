import os
os.system("cls")
'''Determinar el signo'''
print("")
n= int(input("ingresar un numero"))

if n > 0:
    print("numero positivo")
elif n < 0:
    print("numero negativo")
else:
    print("numero neutro")