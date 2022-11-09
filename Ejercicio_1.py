import os 
os.system("cls")

unidades = int(input("Unidades: "))

precio = 25
if unidades <= 25 : precio = 27
elif unidades >= 51 : precio = 23

compra = unidades * precio
descuento = (0.15 if unidades > 50 else 0.05) * compra

print(f"Precio = {precio}\n")
print(f"Compra = {compra}\n")
print(f"Descuento = {precio}\n")
print(f"Total = {compra - descuento}\n")