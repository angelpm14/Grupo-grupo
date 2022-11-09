#inicio

"Un estudiante recibe una propina mensual S/. 20. El estudiante rinde mensualmente tres exámenes." 
"Su papá ha decidido incentivarlo dándole una propina adicional de S/. 5 por cada examen aprobado."
"Desarrolle el programa que determine el monto total de la propina."

primer_examen=float(input("poner el primer número:"))
segundo_examen=float(input("poner el segundo número"))
tercer_examen=float(input("poner el tercer número"))

#proceso 

propina=20

if(primer_examen>14):propina+5
if(segundo_examen>15):propina+5
if(tercer_examen>13):propina+5

print("valor de la propina",propina)

