#inicio

"Una tienda ofrece un porcentaje de descuento sobre el importe de la compra de los cuatro tipos de"
"productos cuyos códigos, precios unitarios y descuentos se muestran en las siguientes tablas. "
"Desarrolle el programa que determine el importe de la compra, el descuento y el total a pagar "
"por la compra de cierta cantidad de unidades de un mismo tipo de producto."

codigo=float(input("escribir valor de codigo:"))
unidades_adquiridas=float(input("ingresar el valor de inudades adquiridas:"))

#proceso

importe_del_descuento=0
precio_unitario=0

if codigo==101: 
    precio_unitario=17
if codigo==102:
    precio_unitario=25
if codigo==103:
    precio_unitario=16
if codigo==104:
    precio_unitario=27

importe_de_la_compra=precio_unitario*unidades_adquiridas
if unidades_adquiridas>=1 and unidades_adquiridas<=10:
    importe_del_descuento=importe_de_la_compra*0.05
if unidades_adquiridas>=11 and unidades_adquiridas<=20:
    importe_del_descuento=importe_de_la_compra*0.08
if unidades_adquiridas>=21 and unidades_adquiridas<=30:
    importe_del_descuento=importe_de_la_compra*0.1
if unidades_adquiridas>31:
    importe_del_descuento=importe_de_la_compra*0.13

importe_a_apagar=importe_de_la_compra-importe_del_descuento
print("valor de importe a pagar:"+repr(importe_a_apagar))
print("valor de importe de la compra:"+repr(importe_de_la_compra))
print("valor de importe del descuento:"+repr(importe_del_descuento))
print("valor de precio unitario:"+repr(precio_unitario))


