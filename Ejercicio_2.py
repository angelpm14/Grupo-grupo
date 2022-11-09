import os
os.system("cls")

unidades = int(input("unidades : "))

precio = 20

if unidades >=1 and unidades <= 50 : caramelos = 5
elif unidades <= 51 and unidades <= 100 : caramelos = 10
else : caramelos = 15

compra = unidades * precio
descuento = ( 0.15 if unidades > 50 else 0.05) * compra

print ( f"Precio = {precio}\n" )
print ( f"Compra = {compra}\n" )
print ( f"Descuento = {precio}\n" )
print ( f"Total = {compra - descuento} mas {caramelos} caramelos \n" )