

#promedios finales
prome_1 = int(input("Ingrese primera nota de practica: "))
prome_2 = int(input("Ingrese segunda nota de practica: "))
prome_3 = int(input("Ingrese tercera nota de practica: "))

if prome_3 >= 10 :
    prome_3 += 2
    print("Mas los puntos extra de la tercera practica: ",prome_3)

else: prome_3 < 10

promedio = prome_1 + prome_2 + prome_3 / 3

print("El promedio final es: ",promedio)
