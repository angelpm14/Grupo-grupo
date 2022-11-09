#inicio

"desarrolle el programa que lea tres números enteros y determine el número intermedio."

primer_número=input("escribir el primer número:")
segundo_número=input("escribir el segundo número:")
tercer_número=input("escribir el tercer número:")

if primer_número>segundo_número:
    medio=primer_número 
    xtem=segundo_número

else:
    medio=segundo_número
    xtem=primer_número

if medio > tercer_número:
    medio=tercer_número

if medio < xtem:
    medio=xtem

print("el número medio es:",medio)





