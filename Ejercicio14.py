#inicio 

"En un supermercado hay una promoción según la cual el cliente raspa una tarjeta que contiene un número oculto."
"Si el número de la tarjeta es par no menor de 100, el cliente obtiene un descuento del 15 %,"
"caso contrario será del 5 % sobre el importe de la compra.  Desarrolle el programa que muestre "
"el número de la tarjeta, el monto de la compra y el descuento."

número=int(input("escribir el número:"))
importe_compra=int(input("escribir el importe de compra:"))

número_int=int(número)
if int(número>100):
    importe_descuento=0.15*importe_compra

else:
    importe_descuento=0.05*importe_compra 
    

print("importe de descuento",importe_descuento)
print("importe de pago",importe_compra-importe_descuento)








